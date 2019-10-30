<p><h1>
<?php

session_start();
if( isset($_SESSION['user'])!="" ){
 header("Location: resetpassword.php");
}
include_once 'connect.php';

if ( isset($_SELECT['sca']) ) {
 $username = trim($_SELECT['username']);
 $email = trim($_SELECT['email']);
 
 //$query = "insert into account(pass) values(?)";
 //$stmt = $pdo->prepare($query);
 $stmt->execute([$username and $email]);
 $row = $stmt->rowCount();

  if ($row == $username and $email) {
   unset($username);
   unset($email);
   unset($pass);
   header("Location: resetpassword.php");
  }
  else
  {
   $message = "Failed! You are not the real account holder!";
  }
}
?>
</h1></p>

<h2>Enter the Email of Your Account to Reset New Password</h2>
<?php echo !empty($statusMsg)?'<p class="'.$statusMsgType.'">'.$statusMsg.'</p>':''; ?>
<div class="container">
    <form action="forgotpassword.php" method="post" name="users" onsubmit="returnVaidate(JSScript.js)">
        <input type="username" name="username" placeholder="Username">
		<input type="email" name="email" placeholder="Email Address">
            <input type="submit" name="sca" value="Submit">
    </form>
</div>