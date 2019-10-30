<?php

$connect = mysql_connect(“create account”, “RyanAdmin”, “C0rBr@y524831”); if (!connect) { die('Connection Failed: ' . mysql_error()); { mysql_select_db(“database_name”, $connect);
$user_info = “INSERT INTO table_name (Username, Password, First Name, Last Name, Gender, Address, City, State, Zip Code) VALUES ('$_POST[username]', '$_POST[password]', '$_POST[first name]','$_POST[last name]', '$_POST[gender]', '$_POST[address]','$_POST[city]','$_POST[state]','$_POST[zip code]')”; if (!mysql_query($user_info, $connect)) { die('Error: ' . mysql_error()); }

echo “Your information was added to the database.”;

mysql_close($connect); ?>