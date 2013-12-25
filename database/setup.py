import os
import re
from dbtools import get_cursor, delete_db, init_db, insert_db

image_dir = "/srv/GoldenPhoenix/assets/img/gallery"

def get_color(f):
    print f
    return "red"

if __name__ == "__main__":
    c = get_cursor()
    #Delete the database and recreate it using the existing schema.
    delete_db(c)
    init_db(c)
    print("Database recreated.")
    dress = 0
    for path in os.walk(image_dir):
        if path[0].find('unused') != -1:
            continue
        else:
            for filename in path[2]:
                insert_db(c, dress, get_color(path[0]+'/'+filename),
                          re.findall('\w+$', path[0])[0], filename,
                          re.findall('assets.*$', path[0])[0],
                          "No description.");
                dress += 1
