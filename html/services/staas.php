<?php
session_start();
if(!isset($_SESSION['user'])){
	echo "login first";
	die();	
}



?>


<html>
<head>
	<script>
		function move() {
		  //document.getElementById("myProgress").style.display = "block"
		  var elem = document.getElementById("myBar");   
		  var width = 10;
		  var id = setInterval(frame, 100);
		  function frame() {
		    if (width >= 100) {
		      clearInterval(id);
		    } else {
		      width++; 
		      elem.style.width = width + '%'; 
		      elem.innerHTML = width * 1  + '%';
		    }
		  }
		}
</script>
	<style type="text/css">
		body{
			background: url(/static/hdbg.jpg) repeat;
		}
		#myProgress {
		  width: 100%;
		  background-color: #ddd;
		}

		#myBar {
		  width: 10%;
		  height: 30px;
		  background-color: #4CAF50;
		  text-align: center;
		  line-height: 30px;
		  color: white;
		}
	</style>
</head>

	
<body>
	<h1> <span style="color:blue;"><i>STAAS</i></span></h1>
	<h3>For linuix users</h3>
	<form action="/cgi-bin/aws/st.py" method="POST">
		<input type="hidden" name="uname" value="<?php  echo $_SESSION['user']  ?>" >
		<input type="text" name="dname" placeholder="enter the drive name"><br><br>
		<input type="text" name="dsize" placeholder="enter the drive size"><br><br>
		<input type="submit" value="submit" name="submit">
	</form><br><br><br>

	<h3>For windows users</h3>

	<form action="/cgi-bin/cifs.py">
		<input type="text" name="dname" placeholder="enter the drive name"><br><br>
		<input type="text" name="dsize" placeholder="enter the drive size"><br><br>
		<input type="submit" value="submit" name="submit">
	</form><br><br><br>
<div style="position:absolute;left:500px;bottom:290px;">
	<h3>Wanna raw storage:-</h3>

	<form action="/cgi-bin/blockst.py">
		<input type="text" name="dname" placeholder="enter the drive name"><br><br>
		<input type="text" name="dsize" placeholder="enter the drive size"><br><br>
		<input type="submit" value="submit" name="submit">
	</form><br><br><br>
</div>




<form action="/cgi-bin/drive.py" method="post">
<input type="hidden" value="qwerty" name="secret_key">
<input type="hidden" value="<?php echo $_SESSION['user']  ?>" name="user">
<input type="submit" value="View Disk">
</form>
<h3>Upload</h3>
<form action="/php/upload.php" method="post" enctype="multipart/form-data">
<select name="drive">
<?php 
session_start();
$user = $_SESSION['user'];
$x=scandir("/var/www/html/users/$user");
?> 
<?php foreach($x as $count=>$y){
	if($count<2)
		continue;
?>
<option value="<?php echo $y ?>"><?php echo $y ?></option>
<?php } ?>
</select><br><br>
 <input id='upload' name="upload[]" type="file" multiple="multiple" /><br><br>
<input type="submit" value="upload" name="submit">


</form>

<form action="/cgi-bin/aws/webserver.py" method="post">
<input type="hidden" value="<?php echo $_SESSION['user'] ?>" name="user">
<input type="submit" value="Want a web server">
</form>





	<div id="myProgress" style="display:none">
  		<div id="myBar">10%</div>
	</div>

</body>
</html>
