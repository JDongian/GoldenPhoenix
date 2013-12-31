from shutil import copyfile
from os import walk
import sys
import re
import resize

image_dir = "/srv/GoldenPhoenix/assets/img/gallery/"
thumb_dir = "/srv/GoldenPhoenix/assets/img/gallery/thumbs/"
ignore = ("METADATA", "*.swp", "INFO")

def matches(ig, f):
    if f in ig:
        return True
    for i in ig:
        if i[0] == '*' and re.findall("\.[^\.]+$", f)[0] == i[1:]:
            return True

def create_thumb(path, f):
    print f, '    \r',
    sys.stdout.flush()
    #TODO: eventually give the thumb a different name.
    try:
        copyfile(path+'/'+f, thumb_dir+f)
        resize.downsize(f)
    except:
        print "Failed on:", f

if __name__ == "__main__":
    metadata = open(image_dir+'METADATA').read()
    lines = (re.findall("(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\"(.*)\"\s+(\d+)", l) if\
             (l and l[0] != '#') else None for l in metadata.split('\n')[:-1])
    lines = [l[0] for l in lines if l]
    #TODO: if != 'NULL' else None
    metadata = { e[0]: { 'filename': e[0],
                         'dress_id': int(e[1]),
                         'category': e[2],
                         'color': e[3],
                         'phototype': e[4],
                         'thumbname': e[5],
                         'description': e[6],
                         'price': e[7] } for e in lines }
    print metadata.keys()
    for path in walk(image_dir):
        if path[0].find('unused') != -1:
            continue
        else:
            for filename in path[2]:
                if matches(ignore, filename) or not (filename in metadata.keys()):
                    continue
                create_thumb(path[0], filename)
    print "Done."
