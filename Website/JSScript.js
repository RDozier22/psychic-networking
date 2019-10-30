<script>
	function Validate() {
		var un = document.forms["accountcreate"]["username"].value;
		if (un == "") {
			alert("Please choose a username");
			return false;
		if (un.length < 5) {
			alert("Please enter a Username at least 5 characters long.")
			return false;
		if (un.length > 15) {
			alert("Please enter a Username no more than 15 characters long.")
			return false;
		}
	
		var x = document.forms["accountcreate"]["fname"].value;
		if (x == "") {
			alert ("Please provide your First Name");
			return false;
		}
		
		var y = document.forms["accountcreate"]["lname"].value;
		if (y == "") {
			alert ("Please provide your Last Name");
			return false;
		}
		
		var z = document.forms["accountcreate"][""].value;
		if (z == "") {
			alert ("Please provide your email address");
			return false;
		}
		
		var password = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/; document.forms["accountcreate"]["password"].value;
		if (password == "") {
			alert ("Please provide your password");
			return false;
		if (password != re-enterpassword)
			alert ("Passwords do not match");
			return false;
		if (inputtxt.value.match(password))
			alert ("Password must contain an Uppercase, Lowercase, Number and Special Character.")
			return false;
		}
		 plength = password.length;
		if (plength <= 10) {
			alert("Your password is not long enough")
			return false;
			}
	}
<script>