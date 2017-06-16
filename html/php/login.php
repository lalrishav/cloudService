<?php
/*if(!isset($_POST['submit'])){
	die();
}*/

$user = $_POST['user'];
$password = $_POST['password'];

if($password=="redhat"){
	exec("sudo mkdir /var/www/html/users/$user");
	exec("sudo mkdir /database/$user");
	exec("sudo chmod 777 /database/$user");
	exec("sudo mkdir /var/www/html/database/$user");
	exec("sudo chmod 777 /var/www/html/database/$user");
	session_start();
	$_SESSION['user']=$user;
	//echo exec("sudo useradd $user");
	//echo exec("echo $password|sudo passwd $user --stdin");

      header("Location:/fe/");
}




?>
