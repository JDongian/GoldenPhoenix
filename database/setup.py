import os
import re
from dbtools import get_cursor, delete_db, init_db, insert_db

image_dir = "/srv/GoldenPhoenix/assets/img/gallery"
ignore = ("METADATA", "*.swp")
metadata = {}

def matches(ig, f):
    if f in ig:
        return True
    for i in ig:
        if i[0] == '*' and re.findall("\.[^\.]+$", f)[0] == i[1:]:
            return True

def get_dress(f):
    try:
        return metadata[filename][1]
    except:
        return "unknown"

def get_color(f):
    try:
        return metadata[filename][0]
    except:
        return "unknown"

def parse_metadata():
    global metadata
    metadata = open(image_dir+'/METADATA').read()
    lines = (l.split(' ') for l in metadata.split('\n')[:-1])
    metadata = {e[0]: e[1:] for e in lines}

if __name__ == "__main__":
    parse_metadata()
    c = get_cursor()
    #Delete the database and recreate it using the existing schema.
    delete_db(c)
    init_db(c)
    print("Database recreated.")
    #dress = 0
    for path in os.walk(image_dir):
        if path[0].find('unused') != -1:
            continue
        else:
            for filename in path[2]:
                if matches(ignore, filename):
                    continue
                insert_db(c, get_dress(filename), get_color(filename),
                          re.findall('\w+$', path[0])[0], filename,
                          re.findall('assets.*$', path[0])[0],
                          "No description.");
                #insert_db(c, dress, get_color(path[0]+'/'+filename),
                #          re.findall('\w+$', path[0])[0], filename,
                #          re.findall('assets.*$', path[0])[0],
                #          "No description.");
                #dress += 1
