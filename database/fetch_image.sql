SELECT filename, location, description, price
FROM gallery_images
WHERE category = %(category)s
ORDER BY dressname, color, image_id
LIMIT %(limit)s
OFFSET %(i)s;
