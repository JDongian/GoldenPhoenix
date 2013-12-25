INSERT INTO gallery_images(
 dressname,
 color,
 category,
 filename,
 thumbfile,
 location,
 description
) VALUES (
    %(dress)s,
    %(color)s,
    %(category)s,
    %(filename)s,
    %(thumbfile)s,
    %(location)s,
    %(description)s
);
