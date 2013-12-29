import os
import psycopg2

def get_cursor(level=0, db="goldenphoenix", user=os.getlogin()):
    """Returns a cursor connected to the given database using given
    credentials. Default level 0 isolation level (autocommit on).
    """
    try:
        conn = psycopg2.connect("dbname={0} user={1}".format(db, user))
        #Execute all actions immediately
        #TODO: properly handle transacitons
        conn.set_isolation_level(level)
        print("Successful database connection.")
    except:
        print("Database connection failed.")
    return conn.cursor()

def delete_db(c):
    """Delete all data.
    """
    c.execute(open("delete.sql", 'r').read())

def init_db(c):
    """Create tables.
    """
    c.execute(open("schema.sql", 'r').read())

def insert_db(c, data):
    if data['phototype'] == 'NULL':
        data['phototype'] = None
    if data['category'] == 'NULL':
        data['category'] = None
    c.execute(open("insert_image.sql", 'r').read(), data)

def fetch_image_db(c, category, offset, limit=1):
    data = {'i': offset,
            'limit': limit,
            'category': category}
    c.execute(open("fetch_image.sql", 'r').read(), data)
    return c.fetchall()

def count_db(c, category):
    data = {'category': category}
    c.execute(open("count_image.sql", 'r').read(), data)
    return c.fetchall()
