"""Adopted from http://stackoverflow.com/a/3244061/2534876
"""

import struct
import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5

def crop(f):
    """Takes in an absolute path.
    Returns the most dominant color in the center of the image.
    """
    im = Image.open(f)
    top = int(im.size[1]*0.6)
    left = int(im.size[0]*0.4)
    bot = int(im.size[1]*0.8)
    right= int(im.size[0]*0.6)
    box = (left, top, right, bot)
    area = im.crop(box)
    return area

def analyze(f):
    """Return the hex value of the most dominant color in the image.
    """
    im = crop(f)
    im = im.resize((128, 128))
    ar = scipy.misc.fromimage(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2])

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    #print 'cluster centres:\n', codes

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    colour = ''.join(chr(c) for c in peak).encode('hex')
    #print 'most frequent is %s (#%s)' % (peak, colour)
    return colour[1:]
