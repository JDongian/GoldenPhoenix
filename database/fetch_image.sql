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
ORDER BY color, dress_id, image_id DESC
LIMIT %(limit)s
OFFSET %(i)s;
