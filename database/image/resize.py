"""Resize all the thumbnails to a smaller resolution for the web.
"""

from PIL import Image
import os, sys

thumbdir = "/srv/GoldenPhoenix/assets/img/gallery/thumbs/"

def downsize(name, w=236):
    print name, '\r',
    sys.stdout.flush()
    im = Image.open(thumbdir+name)
    #Don't resize if it's not worth it.
    if im.size[0]-50 < w:
        return
    scale = float(w)/im.size[0]
    new_width = int(im.size[0]*scale)
    new_height = int(im.size[1]*scale)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.save(thumbdir+name)

if __name__ == "__main__":
    for f in os.listdir(thumbdir):
        downsize(f)
    print "Done.              "
