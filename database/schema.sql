CREATE TYPE cat AS ENUM ('party', 'jacket', 'wedding', 'mens', 'child');
CREATE TYPE photo AS ENUM ('portrait', 'full', 'half', 'back');
CREATE TABLE gallery_images(
 image_id       serial  PRIMARY KEY
,dress_id       integer DEFAULT -1
,category       cat
,color          text    DEFAULT 'unknown'
,phototype      photo   DEFAULT 'half'
,filename       text
,thumbfile      text
,location       text
,description    text    DEFAULT 'No description.'
,price          int     DEFAULT 0
);

