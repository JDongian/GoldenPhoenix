CREATE TABLE gallery_images(
 image_id       serial  PRIMARY KEY,
 dress_id       integer,
 category       text,
 filename       text,
 location       text,
 description    text
);

