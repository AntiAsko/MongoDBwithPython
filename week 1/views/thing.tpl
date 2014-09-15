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
<p>
<form action="/favorite_thing" method="POST">
Favorite thing?
<input type="text" name="thing" size="40" value=""><br>
<input type="submit" value="Submit">
</form>
</body>
</html>
