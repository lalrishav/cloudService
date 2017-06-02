<?php

$login = 'foo';
$pass = 'pass';
$hash = base64_encode(sha1($pass, true));

$contents = $login . ':{SHA}' . $hash;

file_put_contents('/etc/httpd/.htpasswd', $contents);
echo "done"

?>
