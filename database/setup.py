import os
import re
import sys
import imp
from dbtools import get_cursor, delete_db, init_db, insert_db
dominant = imp.load_source('dominant', './image/dominant.py')
classifier = imp.load_source('classifier', './image/classifier.py')

color_ref = classifier.get_ref()
image_dir = "/srv/GoldenPhoenix/assets/img/gallery"
ignore = ("METADATA", "*.swp")
metadata = {}

def matches(ig, f):
    if f in ig:
        return True
    for i in ig:
        if i[0] == '*' and re.findall("\.[^\.]+$", f)[0] == i[1:]:
            return True

def get_description(f):
    try:
        return metadata[filename][3]
    except:
        return "No description."

def get_price(f):
    try:
        return metadata[filename][2]
    except:
        return -1

def get_dress(f):
    try:
        return metadata[filename][1]
    except:
        return "unknown"

def get_color(f, path):
    try:
        return metadata[filename][0]
    except:
        c = classifier.best_match(int(dominant.analyze(path+'/'+f), 16), color_ref)
        print "Calculated best color match:", c, '            \r',
        sys.stdout.flush()
        return c

def parse_metadata():
    global metadata
    metadata = open(image_dir+'/METADATA').read()
    lines = (re.findall("(\S+)\s+(\S+)\s+(\S+)\s+(\d+)\s+\"(.*)\"", l) for l in metadata.split('\n')[:-1])
    lines = [l[0] for l in lines if l]
    metadata = {e[0]: e[1:] for e in lines}

if __name__ == "__main__":
    parse_metadata()
    c = get_cursor()
    #Delete the database and recreate it using the existing schema.
    delete_db(c)
    init_db(c)
    print("Database recreated.")
    for path in os.walk(image_dir):
        if (path[0].find('unused') != -1) or (path[0].find('thumbs') != -1):
            continue
        else:
            for filename in path[2]:
                if matches(ignore, filename):
                    continue
                insert_db(c, get_dress(filename), get_color(filename, path[0]),
                          re.findall('\w+$', path[0])[0], filename,
                          re.findall('assets.*$', path[0])[0],
                          get_description(filename), get_price(filename));
