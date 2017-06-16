<?php
$bucket = $_GET['b'];

?>
<form action="/cgi-bin/fe/uploadfile.py" method="post">
<input type="text" placeholder="enter the path" name="path"><br><br>
<input type="hidden" value="<?php echo $bucket ?>" name="bucket">
<input type="submit" value="upload">
