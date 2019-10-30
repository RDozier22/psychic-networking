<?php
 session_start();
 unset($_SESSION['user']);
 session_unset();
 session_destroy();
 header("Location: index.php");
 exit;
?>

<html>
	<head>
		<title>Logout Page</title>
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
	 Logout and have a nice day
	 <a href='indexpage.php ;'><button>Logout</button></a><br>
	 </a>
	 </p>
    </div>
</body>
</html>
