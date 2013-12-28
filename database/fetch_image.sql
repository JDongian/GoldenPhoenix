SELECT
 category
,color
,phototype
,filename
,thumbfile
,location
,description
,price
FROM gallery_images
WHERE category = %(category)s
ORDER BY filename--dressname, color, image_id DESC
LIMIT %(limit)s
OFFSET %(i)s;
