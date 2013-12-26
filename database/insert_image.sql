INSERT INTO gallery_images(
 dressname,
 color,
 category,
 filename,
 thumbfile,
 location,
 description,
 price
) VALUES (
    %(dress)s,
    %(color)s,
    %(category)s,
    %(filename)s,
    %(thumbfile)s,
    %(location)s,
    %(description)s,
    %(price)s
);
