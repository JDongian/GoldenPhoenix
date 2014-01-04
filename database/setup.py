import os
import re
import sys
import imp
from dbtools import get_cursor, delete_db, init_db, insert_db
#load image classifier tools
dominant = imp.load_source('dominant', './image/dominant.py')
classifier = imp.load_source('classifier', './image/classifier.py')

#color_ref = classifier.get_ref()
image_dir = "/srv/GoldenPhoenix/assets/img/gallery"
ignore = ("METADATA", "*.swp")
metadata = {}

def matches(ig, f):
    if f in ig:
        return True
    for i in ig:
        if i[0] == '*' and re.findall("\.[^\.]+$", f)[0] == i[1:]:
            return True

def get_color(path_to_file):
    try:
        return metadata[filename][0]
    except:
        c = classifier.best_match(int(dominant.analyze(path_to_file), 16), color_ref)
        print "Calculated best color match:", c, '            \r',
        sys.stdout.flush()
        return c

def parse_metadata():
    global metadata
    metadata = open(image_dir+'/METADATA').read()
    #TODO: refactor the regex so that it checks number of \S+'s, not hardcoding cols.
    lines = (re.findall("(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\"(.*)\"\s+(\d+)", l) if\
             (l and l[0] != '#') else None for l in metadata.split('\n')[:-1])
    lines = [l[0] for l in lines if l]
    #TODO: if != 'NULL' else None
    metadata = { e[0]: { 'filename': e[0],
                         'dress_id': int(e[1]),
                         'category': e[2],
                         'gender': e[3] == "female",
                         'color': e[4],
                         'phototype': e[5],
                         'thumbname': e[6],
                         'description': e[7],
                         'price': e[8] } for e in lines }

if __name__ == "__main__":
    parse_metadata()
    print("Metadata parsed for {} valid entries.".format(len(metadata.keys())))
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
                if filename in metadata.keys():
                    data = { 'dress_id': metadata[filename].get('dress_id', 'NULL'),
                             'category': metadata[filename].get('category', 'NULL'),
                             'gender': metadata[filename].get('gender', 'NULL'),
                             'color': metadata[filename].get('color', 'NULL'),
                             'phototype': metadata[filename].get('phototype', 'NULL'),
                             'filename': metadata[filename].get('filename', 'NULL'),
                             'thumbname': metadata[filename].get('thumbname', 'NULL'),
                             'location': re.findall('assets.*$', path[0])[0],
                             'description': metadata[filename].get('description', 'NULL'),
                             'price': metadata[filename].get('price', 'NULL') }
                    if data['color'] == 'NULL':
                        data['color'] = get_color(path[0]+'/'+data['filename'])
                    insert_db(c, data)
                else:
                    pass
