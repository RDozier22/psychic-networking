<p><h1>
<?php
session_start();
require_once 'connect.php';

if(!isset($_SESSION['user'])){
 header("Location: indexpage.php");
 exit;
}
$query = "SELECT * FROM account WHERE userid=?";
$stmt = $pdo->prepare($query);
$stmt->execute([$_SESSION['user']]);
$userRow = $stmt->fetch(PDO::FETCH_ASSOC);
?>
</h1></p>

<html>
	<head>
		<title>Welcome Page</title>
		<meta charset="utf-8">
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<LINK REL=StyleSheet HREF="text.css" TYPE="text/css" MEDIA=screen>
   </style> 
</head>
  <head><title>You are logged in!</title></head>
  </body>
	<div>
	<h1>Ryan's Crypto Bank Profile Page</h1>
	Welcome you have been logged in:
	<?php echo $userRow['fname']; ?>
	<br>
	<br>
	Use the button below to logout of your account.
	<br>
	<br>
	<a href="logout.php" ;><button>Logout</a><br>
	</div>
</body>
</html>