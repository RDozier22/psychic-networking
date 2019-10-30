<p><h1>
<?php
session_start(); 
if( isset($_SESSION['user'])!="" ){
 header("Location: profile.php");
}
include_once 'connect.php';
  
if ( isset($_POST['sca']) ) {
 $username = trim($_POST['username']);
 $pass = trim($_POST['pass']);
 $password = hash('sha256', $pass);

 $query = "select username, pass from account where username=?";
 $stmt = $pdo->prepare($query);
 $stmt->execute([$username]);
 $count = $stmt->rowCount();
 $row = $stmt->fetch(PDO::FETCH_ASSOC);

 if( $count == 1 && $row['pass']==$password ) {
  $_SESSION['user'] = $row['username'];
  header("Location: profile.php"); 
  }
 else {
  header("Location: mariokart.php");
 }
}
?>
</h1></p>

<html>
	<head>
		<title>Login Page</title>
		<meta charset="utf-8">
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<LINK REL=StyleSheet HREF="text.css" TYPE="text/css" MEDIA=screen>
   </style>
</head>
<body>

<form action="Loginpage.php" method="post">
  <div>
	 <h1>Ryan's Crypto Bank</h1>
     <p>
	 Login to access your Super Cool and Awesome Wallet!
	 </p>
	 Username:<br>
	 <input type="text" name="username"><br>
	 <br>
	 Password:<br>
	 <input type="password" name="pass"><br>
	 <br>
	 <input type="submit" name="sca" value="Login">
	 <a href="forgotpassword.php"><button>Forgot Password</a>
  </div>
</body>
</html>
	
