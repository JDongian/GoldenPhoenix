INSERT INTO gallery_images(
 dress_id
,category
,gender
,color
,phototype
,filename
,thumbname
,location
,description
,price
) VALUES (
 %(dress_id)s
,%(category)s
,%(gender)s
,%(color)s
,%(phototype)s
,%(filename)s
,%(thumbname)s
,%(location)s
,%(description)s
,%(price)s
);
