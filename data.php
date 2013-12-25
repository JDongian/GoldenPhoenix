<?php
echo json_encode(json_decode(file_get_contents(sprintf("http://localhost:5000/%s/%d", $_GET['cat'], $_GET['index']))));
//echo file_get_contents(sprintf("http://localhost:5000/%s/%d", $_GET['cat'], $_GET['index']));
?>
