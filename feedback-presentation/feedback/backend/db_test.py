import psycopg2

def get_db():
  connection = psycopg2.connect(user = "admin",
                              password = "admin",
                              host = "127.0.0.1",
                              port = "5432",
                              database = "feedback")
  cursor = connection.cursor()
  # Print PostgreSQL Connection properties
  print ( connection.get_dsn_parameters(),"\n")
  return cursor, connection

def close_db(cursor, connection):
  cursor.close()
  connection.close()


def create_tables(conn):
    commands = (
        """
        CREATE TABLE surveys (
                _id INTEGER PRIMARY KEY,
                survey_type VARCHAR(255) NOT NULL,
                response INTEGER NOT NULL
        )
        """,
        """
        CREATE TABLE reports (
                _id INTEGER PRIMARY KEY,
                survey_type VARCHAR(255) NOT NULL,
                average_response INTEGER NOT NULL
        )
        """)
    try:
        cursor = conn.cursor()
        for command in commands:
          cursor.execute(command)
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def find_all(cursor):
  surveys = cursor.fetchall()
  return surveys

def calculate_avg(surveys):
  avg = 0
  for survey in surveys:
    avg += survey[3]
  return float(avg) / len(survey)

def insert_test_data(cursor, conn, my_id):
    query = '''
      INSERT INTO public.surveys
      (_id, survey_type, response) VALUES (%s, %s, %s) RETURNING _id, survey_type, response;
    '''
    values = (my_id, "test", 3)
    cursor.execute(query, values)
    conn.commit()