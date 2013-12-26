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
    print f, '\r',
    sys.stdout.flush()
    #TODO: eventually give the thumb a different name.
    try:
        copyfile(path+'/'+f, thumb_dir+f)
        resize.downsize(f)
    except:
        print "Failed on:", f

if __name__ == "__main__":
    for path in walk(image_dir):
        if path[0].find('unused') != -1:
            continue
        else:
            for filename in path[2]:
                if matches(ignore, filename):
                    continue
                create_thumb(path[0], filename)
    print "Done."
