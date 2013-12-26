from bs4 import BeautifulSoup
import requests
import sys

def squ_diff(c1, c2):
    return ((c1 & 0x0000FF) - (c2 & 0x0000FF))**2 +\
           (((c1 & 0x00FF00)>>8) - ((c2 & 0x00FF00)>>8))**2 +\
           (((c1 & 0xFF0000)>>16) - ((c2 & 0xFF0000)>>16))**2

def best_match(c, ref):
    """Find the best match for color c.
    Uses least square to determine fitness.
    """
    diff = squ_diff(0xFFFFFF, 0x000000)
    best = "None"
    for ref_color in ref:
        curr_diff = squ_diff(c, ref_color[1])
        #if curr_diff < 1000:
        #    print curr_diff, ref_color[0], hex(ref_color[1])
        if curr_diff < diff:
            diff = curr_diff
            best = ref_color[0]
    return best

def get_ref():
    """Retreives some reference colors.
    Format:
        [("red", 0xFF0000), ("green", 0x00FF00), ("blue", 0x0000FF)]
    """
    html = requests.get("http://jadecat.com/tuts/colorsplus.html").content
    soup = BeautifulSoup(html)
    return [(e.text[:-6].strip(), int(e.text[-6:], 16)) for e in soup.find_all("td")[2:]]

if __name__ == "__main__":
    """For testing, just provide a hex value as the argument.
    """
    r = get_ref()
    print best_match(int(sys.argv[1], 16), r)
