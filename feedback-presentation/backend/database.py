#!/usr/bin/env python

import copy
import os
import logging
from collections import namedtuple

from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, ConnectionFailure
import pendulum

from analytics_utils.models import model_factory

DBTuple = namedtuple('DbTuple', ['client', 'database'])

DB_NAME = os.getenv('DB_NAME', 'surveys')
USERNAME = os.getenv('DB_USERNAME', 'admin')
PASSWORD = os.getenv('DB_PASSWORD', 'admin')
DB_URL = os.getenv('DB_URL', 'surveys_db')
DB_SSL = os.getenv('DB_SSL', None)


def get_db(logger=None):
    """Get the DB and client

    The function also updates or creates users, indexes, and collections

    Keyword Arguments:
        logger (logging.Logger): A logger (default: {None})

    Returns:
        pymongo.Client, pymongo.Database -- The client for
         creating transaction sessions & the DB handle
    """

    if logger is None:
        logger = logging.getLogger(__name__)

    logger.info('Connecting to %s at %s', DB_NAME, DB_URL)
    client = MongoClient(DB_URL, username=USERNAME, password=PASSWORD, ssl=bool(DB_SSL))
    database = client[DB_NAME]

    # test that we can connect as recommended in PyMongo docs
    # https://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure as ex:
        logger.error("Server not available: %s", ex)
        raise ex

    logger.info('Connected to %s at %s', DB_NAME, DB_URL)

    return DBTuple(client, database)