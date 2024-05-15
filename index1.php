<?php
header('Content-Type: text/html; charset=UTF-8');

$allowed_referrer = 'https://hazimeteotukai.github.io/scriptdownloadsite/';

if (!isset($_SERVER['HTTP_REFERER']) || strpos($_SERVER['HTTP_REFERER'], $allowed_referrer) !== 0) {
    // リファラーが一致しない場合、403 Forbiddenを返す
    header('HTTP/1.0 403 Forbidden');
    echo 'このページにはアクセスできません。';
    exit;
}
?>
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Index1</title>
</head>
<body>
<h1>index1.htmlへようこそ</h1>
</body>
</html>
