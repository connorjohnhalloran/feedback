from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import ModelType, \
    BaseType, \
    BooleanType, \
    StringType, \
    ListType, \
    IntType, \
    FloatType, \
    UTCDateTimeType, \
    DictType

import pendulum
from bson.objectid import ObjectId


class ObjectIdType(BaseType):
    '''Schematics type implementation for Mongo's ObjectId

    Reference:
        https://schematics.readthedocs.io/en/latest/usage/extending.html
        https://schematics.readthedocs.io/en/latest/usage/types.html

    Extends:
        BaseType

    Variables:
        native_type {factory_func} -- ObjectId constructor function
    '''

    native_type = ObjectId

    def to_primitive(self, value, context=None):
        ''' Get the primitive representation of the type which is a string'''
        return str(value)

    def validate_object_id(self, value, context=None):
        ''' Make sure that the value is an instance of ObjectId '''
        if not isinstance(value, ObjectId):
            raise ValidationError(
                '"{}" is not an instance of ObjectId'.format(value))


class Surveys(Model):
    survey_type = StringType(required=True)
    happy = BooleanType(required=True)
    sad = BooleanType(required=True)
    indifferent = BooleanType(required=True)