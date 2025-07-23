<!DOCTYPE html>
<?php
session_start();
if($_SERVER['HTTP_REFERER'] == "" )

{
	header("Location: index.php");
}
require_once ('connect_database.php');
$tmp = date("Y-m-d");?>
<html>
<head>
	<meta charset="utf-8">
	<title>User List</title>
	<link rel="Icon" type="image/x-icon" href="images/logo2.ico" />
</head>
<?php
echo '<span style="color: #007979; font-size: 50px;"> ';
echo "&thinsp;Hello,".$_SESSION['username'];
echo '</span>';

?>
<style>
.box {
  position: relative;
  top: 0;
  opacity: 1;
  float: left;
  padding: 12% 10% 8% 10%;
  width: 100%;
  background: #D1E9E9;
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
.input label, .input input, .input .spin {
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
  margin-top: 20px;
  height: 70px;
}

.input {
  position: relative;
}
.input input {
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
  margin: 2% 0%;
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
  font-size: 16px;
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
  margin-top: 5px;
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
.overbox .title, .overbox .button, .overbox .input {
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
.overbox .material-button, .overbox .alt-2 {
  display: block;
}
.overbox .material-button .shape, .overbox .alt-2 .shape {
  display: block;
}

body {
  background-image: url("images/smedtrum_background3.jpg");
  background-position: center;
  background-size: 100% 100%;
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
  max-width: 500px;
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
</style>

<div class="materialContainer">


   <div class="box">

      <div class="title">View users/Delete</div>
		  <div id="root">
		  <table id="tbl" style="width:100%;text-align:center;" border="1">
			<thead>
			<tr>
				<td>No.</td>
				<td>Username</td>
				<td></td>
			</tr>
			</thead>
			<tbody>
			<?php 
				$connecta = mysqli_query($connect , "select username from users");
				$i = 1;
				while($a = mysqli_fetch_array($connecta)){
					$name = $a['username'];
					echo "<tr><td style='vertical-align:middle;'>".$i."</td>";
					echo "<td style='vertical-align:middle;'>".$name."</td>";?>
					<form method='POST' action='delete_user.php'>
					<input type ='hidden' name='name' value='<?php echo $name;?>'>
					<td><button type="submit" style="background-image: url('images/delete_icon.png');background-size:cover;width:35px;height:35px;vertical-align:middle;" onclick="return confirm('Are you sure to delete <?php echo $name;?>?');"></td></tr>
					</form>
					<?php $i++;
				}
			?>
		  <tbody>
		  </table>
		  <span id='table_page'></span>
		  </div>
		  <div class="button login">
			 <button onclick="window.location.href='register.php';"><span>Back</span> <i class="fa fa-check"></i></button>
		  </div>	  
		  <div class="button login">
			 <button onclick="window.location.href='logout.php';"><span>Main page</span> <i class="fa fa-check"></i></button>
		  </div>
   </div>

</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="jquery-tablepage-1.0.js"></script>
<script>
$("#tbl").tablepage($("#table_page"), 10);

</script>
</html>