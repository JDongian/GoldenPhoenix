CREATE TABLE gallery_images(
 image_id       serial  PRIMARY KEY,
 dressname      text,
 color          text,
 category       text,
 filename       text,
 thumbfile      text,
 location       text,
 description    text,
 price          int
);

