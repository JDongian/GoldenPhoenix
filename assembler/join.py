import re

def asm(template, parts):
    out = re.sub("<%CSS></%CSS>", re.findall("<%CSS>([^~]*)</%CSS>", parts)[0], template)
    out = re.sub("<%BODY></%BODY>", re.findall("<%BODY>([^~]*)</%BODY>", parts)[0], out)
    out = re.sub("<%JS></%JS>", re.findall("<%JS>([^~]*)</%JS>", parts)[0], out)
    return out

if __name__ == "__main__":
    t = open("template.html").read()
    ipart = open("index.part").read()
    gpart = open("index.part").read()
    cpart = open("index.part").read()
    open("index.html", 'w').write(asm(t, ipart))
    open("index.html", 'w').write(asm(t, gpart))
    open("index.html", 'w').write(asm(t, cpart))
