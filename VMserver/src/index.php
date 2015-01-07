<?php // index.php
require_once 'openid.php';
$openid = new LightOpenID("ec2-54-172-243-204.compute-1.amazonaws.com");

$openid->identity = 'https://www.google.com/accounts/o8/id';
$openid->required = array(
  'namePerson/first',
  'namePerson/last',
  'contact/email',
);
$openid->returnUrl = 'http://ec2-54-172-243-204.compute-1.amazonaws.com/login.php'
?>

<a href="<?php echo $openid->authUrl() ?>">Login with Google</a>

