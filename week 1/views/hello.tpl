<!DOCTYPE html>
<html>
<head>
<title>Hey!</title>
</head>
<body>
<p>
Welcome {{username}}
</p>
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
</p>
</body>
</html>
