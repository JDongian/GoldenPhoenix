SELECT
 category
,color
,phototype
,filename
,thumbname
,location
,description
,price
FROM gallery_images
WHERE category = %(category)s
ORDER BY color DESC, dress_id, image_id
LIMIT %(limit)s
OFFSET %(i)s;
