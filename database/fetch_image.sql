SELECT filename, location, description
FROM gallery_images
WHERE category = %(category)s
LIMIT %(limit)s
OFFSET %(i)s;
