SELECT filename, location, description
FROM gallery_images
WHERE category = %(category)s
ORDER BY dressname, color, image_id
LIMIT %(limit)s
OFFSET %(i)s;
