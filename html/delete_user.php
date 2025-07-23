<?php
if($_SERVER['HTTP_REFERER'] == "" )

{
	header("Location: index.php");
}
require_once ('connect_database.php');
$name = $_POST["name"];
$sql = "delete from users where username = '$name'";
if($connect->query($sql) === true){
	echo $name."success";
}
else{
	echo "fail";
}
header("Location: user_list.php");
?>