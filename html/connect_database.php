<?php
define("server", "localhost");
define("user", "root");
define("password", "root");
define("database", "smedtrum");
//mysql_connect(); parameters
$connect = mysqli_connect(server, user, password, database);
//run a simple condition to check your connection
$connectc = mysqli_query($connect , "set names utf8");

if (!$connectc)
{
    die("You DB connection has been failed!: " . mysqli_connect_error());
}
?>