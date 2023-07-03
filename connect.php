<?php
    $empid = $_POST['empid'];
	$firstname = $_POST['firstname'];
	$lastname = $_POST['lastname'];
    $email = $_POST['email'];
	$age = $_POST['age'];
	$number = $_POST['number'];
	$pass = $_POST['pass'];
	
	// Database connection
	$conn = new mysqli('localhost','root','','registable');
	if($conn->connect_error){
		echo "$conn->connect_error";
		die("Connection Failed : ". $conn->connect_error);
	} else {
		$stmt = $conn->prepare("insert into registration(empid,firstname,lastname,email,age,number,pass) values(?, ?, ?, ?, ?, ?, ?)");
		$stmt->bind_param("ssssiis", $empid, $firstname, $lastname, $email, $age, $number, $pass);
		$execval = $stmt->execute();
		echo $execval;
		echo "Registration successfully...";
		$stmt->close();
		$conn->close();
	}
?>

