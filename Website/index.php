<p><h1>
<?php
session_start();
if (isset($_SESSION['message'])){	
 echo $_SESSION['message'];
}
?>
</h1></p>

<html>
<body>

</body>
</html>

<html>
	<head>
		<title>Landing Page</title>
		<meta charset="utf-8">
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<LINK REL=StyleSheet HREF="text.css" TYPE="text/css" MEDIA=screen>
   </style> 
</head>
<body>
	<div>
	 <h1>Ryan's Crypto Bank</h1>
     <p>
	 This website has been estbalished in 2019 to provide a secure way of storing your crypto-currency wallet. 
	 We use the bestest encryption standards today to ensure your identity and wallet are secure.
	 <p>
	 Use the below buttons to create a new account or sign in to your current account.
	 </p>
	<a href="AccountCreationpage.php" ;><button>Create Account</a><br>
	<a href="Loginpage.php" ;><button>Login</a>
    </div>
</body>
</html>