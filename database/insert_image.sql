INSERT INTO gallery_images(
 dress_id,
 category,
 filename,
 location,
 description
) VALUES (
    %(dress)s,
    %(category)s,
    %(filename)s,
    %(location)s,
    %(description)s
);
