import os
import re
import psycopg2

image_dir = "/srv/GoldenPhoenix/assets/img/gallery"

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

def insert_db(dress, category, filename, location, description):
    data = {'dress': dress,
            'category': category,
            'filename': filename,
            'location': location,
            'description': description}
    c.execute(open("insert_image.sql", 'r').read(), data)

if __name__ == "__main__":
    c = get_cursor()
    #Delet the database and recreate it using the existing schema.
    delete_db(c)
    init_db(c)
    print("Database recreated.")
    dress = 0
    for path in os.walk(image_dir):
        if path[0].find('unused') != -1:
            continue
        else:
            for filename in path[2]:
                insert_db(dress, re.findall('\w+$', path[0])[0], filename, path[0], "No description.");
                dress += 1
