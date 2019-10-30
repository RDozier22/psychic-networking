<p><h1>
<?php

session_start();
if( isset($_SESSION['user'])!="" ){
 header("Location: Loginpage.php");
}
include_once 'connect.php';

if ( isset($_POST['sca']) ) {
 $username = trim($_POST['username']);
 $email = trim($_POST['email']);
 $fname = trim($_POST['fname']);
 $lname = trim($_POST['lname']);
 $address = trim($_POST['address']);
 $city = trim($_POST['city']);
 $state = trim($_POST['state']);
 $zipcode = trim($_POST['zipcode']);
 $pass = trim($_POST['pass']);
 $password = hash('sha256', $pass);

 $query = "insert into account(username,email,fname,lname,pass,address,city,state,zipcode) values(?, ?, ?, ?, ?, ?, ?, ?, ?)";
 $stmt = $pdo->prepare($query);
 $stmt->execute([$username,$email,$fname,$lname,$password,$address,$city,$state,$zipcode]);
 $rowsAdded = $stmt->rowCount();

  if ($rowsAdded == 1) {
   unset($email);
   unset($fname);
   unset($lname);
   unset($pass);
   unset($address);
   unset($city);
   unset($state);
   unset($zipcode);
   header("Location: loginpage.php");
  }
  else
  {
   $message = "Failed! For some reason unknown to any man, woman or computer!";
  }
}
?>
</h1></p>

<html>
	<head>
		<title>Account Creation Page</title>
		<meta charset="utf-8">
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<LINK REL=StyleSheet HREF="text.css" TYPE="text/css" MEDIA=screen>

   </style> 
</head>
</body>

	<div>
	 <h1>Ryan's Crypto Bank</h1>
     <p>
	 Fill out the below form to create your account.
	 </p>
	 <form action="AccountCreationpage.php" method="post" name="users" onsubmit="returnVaidate(JSScript.js)">
		UserName:<br>
		<input type="text" name="username"><br>
		<br>
		Email Address:<br>
		<input type="text" name="email"><br>
		<br>
		Password:<br>
		<input type="password" name="pass"><br>
		<br>
		Re-enter Password:<br>
		<input type="password" name="re-enterpassword"><br>
		<br>
		First Name:<br>
		<input type="text" name="fname"><br>
		<br>
		Last Name:<br>
		<input type="text" name="lname"><br>
		<br>
		Address:<br>
		<input type="text" name="address"><br>
		<br>
		City:<br>
		<input type="text" name="city"><br>
		<br>
		State:<br>
		<input type="text" name="state"><br>
		<br>
		Zip Code:<br>
		<input type="text" name="zipcode"><br>
		<br>
	    <input type="submit" name="sca" value="Submit">
	</form>
   </div>
</body>
</html>