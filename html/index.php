<!DOCTYPE html>
<?php
session_start();
require_once ('connect_database.php');
?>
<html>
<head>
	<meta charset="utf-8">
	<title>Main Page</title>
	<link rel="Icon" type="image/x-icon" href="images/logo2.ico" />
</head>
<style>
.box {
  position: relative;
  top: 0;
  opacity: 1;
  float: left;
  padding: 60px 50px 40px 50px;
  width: 100%;
  background: #fff;
  border-radius: 10px;
  transform: scale(1);
  -webkit-transform: scale(1);
  -ms-transform: scale(1);
  z-index: 5;
}
.box.back {
  transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -ms-transform: scale(0.95);
  top: -20px;
  opacity: 0.8;
  z-index: -1;
}
.box:before {
  content: "";
  width: 100%;
  height: 30px;
  border-radius: 10px;
  position: absolute;
  top: -10px;
  background: rgba(255, 255, 255, 0.6);
  left: 0;
  transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -ms-transform: scale(0.95);
  z-index: -1;
}

.overbox .title {
  color: #fff;
}
.overbox .title:before {
  background: #fff;
}

.title {
  width: 100%;
  float: left;
  line-height: 46px;
  font-size: 34px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #1aa0a9;
  position: relative;
}
.title:before {
  content: "";
  width: 5px;
  height: 100%;
  position: absolute;
  top: 0;
  left: -50px;
  background: #1aa0a9;
}

.overbox .text-show {
  color: #fff;
}
.overbox .text-show:before {
  background: #fff;
}

.text-show {
  width: 100%;
  float: left;
  line-height: 46px;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: 2px;
  color: #1aa0a9;
  position: relative;
}
.text-show:before {
  content: "";
  width: 5px;
  height: 100%;
  position: absolute;
  top: 0;
  left: -50px;
  background: #1aa0a9;
}

.input {
  transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -ms-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.input label, .input input, .input .spin {
  transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -ms-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

.button {
  transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -ms-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.button button .button.login button i.fa {
  transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -ms-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

.button.login button {
  transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
  -ms-transition: 300ms cubic-bezier(0.4, 0, 0.2, 1);
}

.input {
  width: 100%;
  float: left;
}
.input label, .input input, .input .spin,.input i {
  width: 100%;
  float: left;
}

.button {
  width: 100%;
  float: left;
}
.button button {
  width: 100%;
  float: left;
}

.input, .button {
  margin-top: 30px;
  height: 70px;
}

.input {
  position: relative;
}
.input input {
  position: relative;
}
.input i {
  position: relative;
}

.button {
  position: relative;
}
.button button {
  position: relative;
}

.input input {
  height: 60px;
  top: 6px;
  border: none;
  background: transparent;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  color: rgba(0, 0, 0, 0.8);
  font-weight: 300;
}
.input i {
  height: 60px;
  top: 6px;
  border: none;
  background: transparent;
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  color: rgba(0, 0, 0, 0.8);
  font-weight: 300;
}
.input label {
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  color: rgba(0, 0, 0, 0.8);
  font-weight: 300;
}

.button button {
  font-family: "Roboto", sans-serif;
  font-size: 24px;
  color: rgba(0, 0, 0, 0.8);
  font-weight: 300;
}

.input:before, .input .spin {
  width: 100%;
  height: 1px;
  position: absolute;
  bottom: 0;
  left: 0;
}
.input:before {
  content: "";
  background: rgba(0, 0, 0, 0.1);
  z-index: 3;
}
.input .spin {
  background: #1aa0a9;
  z-index: 4;
  width: 0;
}

.overbox .input .spin {
  background: white;
}
.overbox .input:before {
  background: rgba(255, 255, 255, 0.5);
}

.input label {
  position: absolute;
  top: 10px;
  left: 0;
  z-index: 2;
  cursor: pointer;
  line-height: 60px;
}

.button {
  margin-top: 20px;
  margin: 40px 0;
  overflow: hidden;
  z-index: 2;
}
.button.login {
  width: 60%;
  left: 20%;
}
.button.login button {
  width: 100%;
  line-height: 64px;
  left: 0%;
  background-color: transparent;
  border: 3px solid rgba(0, 0, 0, 0.1);
  font-weight: 900;
  font-size: 18px;
  color: rgba(0, 0, 0, 0.2);
}
.button button {
  width: 100%;
  line-height: 64px;
  left: 0%;
  background-color: transparent;
  border: 3px solid rgba(0, 0, 0, 0.1);
  font-weight: 900;
  font-size: 18px;
  color: rgba(0, 0, 0, 0.2);
}
.button.login {
  margin-top: 80px;
}
.button button {
  background-color: #fff;
  color: #1aa0a9;
  border: none;
}
.button.login button.active {
  border: 3px solid transparent;
  color: #fff !important;
}
.button.login button.active span {
  opacity: 0;
  transform: scale(0);
  -webkit-transform: scale(0);
  -ms-transform: scale(0);
}
.button.login button.active i.fa {
  opacity: 1;
  transform: scale(1) rotate(0deg);
  -webkit-transform: scale(1) rotate(0deg);
  -ms-transform: scale(1) rotate(0deg);
}
.button.login button i.fa {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  line-height: 60px;
  transform: scale(0) rotate(-45deg);
  -webkit-transform: scale(0) rotate(-45deg);
  -ms-transform: scale(0) rotate(-45deg);
}
.button.login button:hover {
  color: #1aa0a9;
  border-color: #1aa0a9;
}
.button button {
  cursor: pointer;
  position: relative;
  z-index: 2;
}

.click-efect {
  position: absolute;
  top: 0;
  left: 0;
  background: #1aa0a9;
  border-radius: 50%;
}

.overbox {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  overflow: inherit;
  border-radius: 10px;
  padding: 60px 50px 40px 50px;
}
.overbox .title, .overbox .button, .overbox .input, .overbox {
  z-index: 111;
  position: relative;
  color: #fff !important;
  display: none;
}
.overbox .title {
  width: 80%;
}
.overbox .input {
  margin-top: 20px;
}
.overbox .input input, .overbox .input label {
  color: #fff;
}
.overbox .material-button, .overbox .alt-2 .i{
  display: block;
}
.overbox .material-button .shape, .overbox .alt-2 .shape .i{
  display: block;
}

body {
  background-image: url("images/smedtrum_background.jpg");
  background-position: center;
  background-size: 123% 123%;
  background-repeat: no-repeat;
  min-height: 100vh;
  font-family: "Roboto", sans-serif;
  overflow: hidden;
}

html {
  overflow: hidden;
}

.materialContainer {
  width: 100%;
  max-width: 460px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}

* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  text-decoration: none;
  list-style-type: none;
  outline: none;
}
*:after, *::before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  text-decoration: none;
  list-style-type: none;
  outline: none;
  
}
.pass-forgot {
  width: 100%;
  float: left;
  text-align: center;
  color: rgba(0, 0, 0, 0.4);
  font-size: 18px;
}
.dialog {
  width: 100%;
  float: left;
  text-align: center;
  font-size: 26px;
  margin-top: 20px;

}
</style>

<div class="materialContainer">


   <div class="box">

      <div class="title">LOGIN</div>

	  <form class="form" method="POST">

		  <div class="input">
			 <font size="4">Username:</font>
			 <input type="text" name="name" id="name" required>
			 <span class="spin"></span>
		  </div>

		  <div class="input">
			 <font size="4">Password:</font>
			 <input type="password" name="pass" id="pass" required>
			 <span class="spin"></span>
		  </div>

		  <div class="button login">
			 <button type="submit" id="login-button" onclick="checkAdmin()"><span>Go</span> <i class="fa fa-check"></i></button>
		  </div>
		  
		  <a href="change_password.php" class="pass-forgot">Forgot your password?</a>
	  </form>
   </div>

</div>
<script>
function checkAdmin()
</script>
<?php
	$name = $_POST['name'];
	$pass = $_POST['pass'];
	$connecta = mysqli_query($connect , "select * from users where id = 1");
	$connectb = mysqli_query($connect , "select username,password,last_login,login_count from users");
	$a = mysqli_fetch_array($connecta);
	if($name == $a['username'] && $pass == $a['password']){
		$_SESSION['username']="$name";
		echo "<script type='text/javascript'>";
		echo "window.location.href='register.php'";
		echo "</script>";
	}
	else{
			$flag = false;
			while($b = mysqli_fetch_array($connectb)){
				if($name == '' && $pass == ''){
					break;
				}
				if($name == $b['username'] && $pass == $b['password']){
					$flag = false;
					openlog("MyScriptLog", 0, LOG_LOCAL0);
					$now = date("Y-m-d H:i:s");
					$now2 = date("Y-m-d");
					$tmp = substr($b['last_login'],0,-9);
					if($tmp != $now2){
						$count = 0;
					}
					else{
						$count = $b['login_count'];
					}
					syslog(LOG_INFO, "Username: ".$name.",login at ".$now);
					$sql = "update users set last_login='$now',login_count='$count' where username = '$name'";
					if($connect->query($sql) === true){
					}
					$_SESSION['username']="$name";
					closelog();
					echo "<script type='text/javascript'>";
					echo "window.location.href='test2.php'";
					echo "</script>";
					break;
				}
				else if($name == $b['username'] && $pass != $b['password']){
					echo "<script type='text/javascript'>";
					echo "alert('Wrong password.');";
					echo "</script>";
					$flag = false;
					break;
				}
				else if($name != $b['username']){
					$flag = true;
				}
			}
			if($flag){
				echo "<script>";
				echo "alert('Invalid user.');";
				echo "</script>";
			}
	}
?>

</html>