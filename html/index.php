<?php
session_start();
if(isset($_SESSION['user'])){
		header("Location:/services.php");
}



?>


<!DOCTYPE>
<html>
	<head>
		
		<title>Hello world</title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		
		<style type="text/css">
			#authentication{
			
				width: 400px;
				height: 200px;
			 	border-style: solid;
    			border-left:3px solid red;
				border-right:3px solid blue;
				border-bottom:3px solid orange;
				border-top:3px solid black;
    			border-style: solid;
			    border-radius: 35px;
			    padding: 50px;
			    background-color: white;
			}
			#shell{
				width: 300px;
				height: 200px;
				border-style: solid;
				border: 1px brown;
				border-style: dotted;
				border-radius: 75px;
				padding: 25px;
				padding-bottom: 00px;
				background-color: white;
				color: green

			}
			#register{
				width: 300px;
				height: 200px;
				border-style: solid;
				border: 1px brown;
				border-style: dotted;
				border-radius: 75px;
				padding: 25px;
				padding-bottom: 50px;
				background-color: white;
				color: green

			}
			#submit{
				width: 75px;
				height: 40px;
				
				border-radius: 60px
			}
		</style>
		<script>
		function hello(){
		        $("#shell").slideUp();
		        $("#register").slideDown();
		        document.getElementById('authentication').style.height = "300px"
		        document.getElementById('bottom').style.display = "none"
		}
		</script>
		<script type="text/javascript">
			var i = 5;
			var x = setInterval(function(){
				//i++;
				
			},500)
		</script>
	</head> 

	<body>
		<center><h1><span style="color:red">Welcome to Our </span><span style="color:blue">Cloud Service</span></h1></center>
		<h3><span style="color:red">We provide all the cloud facilities</span><span style="color:blue"> <b><i>securely</i></b></span> <span style="color:red">and</span> <span style="color:blue"><b><i>cheaply</i></b></span></h3>
		<br><br>
		<center><div id="authentication">
			
			<form id="shell" style="display:block" action="php/login.php" method="POST">
				<center>Login Please</center>
				<br>
				<input type="text" placeholder="Enter your username" name="user">
				<br><br>
				<input type="password" placeholder="Enter your password" name="password"><br><br>
				<input type="submit" id="submit" value="GO">
			</form>

			<form id="register" style="display:none" action="register.php" method="POST">
				<center>Register Here</center>
				<br>
				<input type="text" placeholder="Enter your username" name="user">
				<br><br>
				<input type="text" placeholder="Enter your password" name="password"><br><br>
				<input type="text" placeholder="Again Enter your password" name="repassword"><br><br>

				<input type="submit" id="submit" value="GO" name="register">
			</form>
		</div></center><br>
		<center id="bottom">Don't have an account??<span id="askRegister" onclick="hello()" style="color:blue">Wanna signup Click here??<span></center>
	</body>
</html>
