<?php
header('Content-Type: application/json; charset=iso-8859-1');
echo file_get_contents(sprintf("http://localhost:5000/%s/%d", $_GET['cat'], $_GET['index']));
?>
