<p><h1>
<?php
session_start();
if (isset($_SESSION['message'])){	
 echo $_SESSION['message'];
}
?>
</h1></p>

<html>
	<head>
		<title>Failed Login Page</title>
		<meta charset="utf-8">
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<LINK REL=StyleSheet HREF="text.css" TYPE="text/css" MEDIA=screen>
   </style> 
</head>
<body>

	<div id='maindiv'>
	 <h1>Ryan's Crypto Bank Failed Login Page</h1>
     <p>
	 You failed to login correctly to the Super Duper Awesome Bank Page.<br> 
	 Have fun playing Mario Kart!<br>
	 BYE!!
	 </p>
	  <video src="Super Mario Kart.mp4" id="my_video"></video>
	  <video width="1280" height="720" controls></video>
	  <script type="text/javascript">
		setTimeout(function(){
		  document.getElementById("my_video").play();
        }, 5000)
      </script>
    </div>
</body>
</html>

