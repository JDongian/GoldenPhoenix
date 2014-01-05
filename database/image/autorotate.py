"""Rotate images to the correct orientation.
"""

from PIL import Image
import os, sys

thumbdir = "/srv/GoldenPhoenix/assets/img/gallery/thumbs/"

def autorotate(path, name):
    sys.stdout.flush()
    im = Image.open(path+name)
    #If the image needs rotating, do it.
    if im.size[1] < im.size[0]:
        print 'Rotating:', name, '      '
        im = im.transpose(Image.ROTATE_270)
        im.save(path+name)
    else:
        print 'Skipping:', name, '\r',

if __name__ == "__main__":
    directory = raw_input("dir = ")
    for f in os.listdir(directory):
        autorotate(directory, f)
    #for f in os.listdir(thumbdir):
    #    autorotate(thumbdir, f)
    print "Done.                  "
