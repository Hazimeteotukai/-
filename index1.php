<?php
$allowed_referrer = 'http://yourdomain.com/index.html'; // 必要に応じて正しいURLに変更してください

if (!isset($_SERVER['HTTP_REFERER']) || strpos($_SERVER['HTTP_REFERER'], $allowed_referrer) !== 0) {
    // リファラーが指定されたURLと一致しない場合
    header('HTTP/1.0 403 Forbidden');
    echo 'このページにはアクセスできません。';
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Index1</title>
</head>
<body>
<h1>index1.htmlへようこそ</h1>
</body>
</html>
