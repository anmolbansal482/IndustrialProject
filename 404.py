#!C:\python3.6.8\python.exe
# -*- coding: utf-8 -*-
import cgi
import Cookie

print ("Content-type:text/html\r\n\r\n")
print ("""<!Doctype html>
<html lang="en"> 
<head>
	<title>HelpZone – Knowledge Base / Support HTML Template</title>
	<meta name="description" content="">
	<meta name="keywords" content="">
	<meta charset="utf-8">
	<meta name="author" content="Dmitry Volkov">
	<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1"><![endif]-->
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<!-- Favicons -->
	<link rel="icon" type="image/png" href="../../docs/icon/favicon-16x16.png" sizes="16x16">
	<link rel="icon" type="image/png" href="../../docs/icon/favicon-32x32.png" sizes="32x32">
	<link rel="apple-touch-icon-precomposed" sizes="57x57" href="../../docs/icon/apple-touch-icon-57x57.png">
	<link rel="apple-touch-icon-precomposed" sizes="72x72" href="../../docs/icon/apple-touch-icon-72x72.png">
	<link rel="apple-touch-icon-precomposed" sizes="114x114" href="../../docs/icon/apple-touch-icon-114x114.png">
	<link rel="apple-touch-icon-precomposed" sizes="120x120" href="../../docs/icon/apple-touch-icon-120x120.png">
	<link rel="apple-touch-icon-precomposed" sizes="152x152" href="../../docs/icon/apple-touch-icon-152x152.png">

	<!-- Fonts -->
	<link href='../../fonts.googleapis.com/css.css' rel='stylesheet' type='text/css'>

	<!-- Icons -->
	<link rel="stylesheet" href="../../docs/css/material-design-iconic-font.min.css">

	<!-- CSS -->
	<link rel="stylesheet" href="../../docs/css/bootstrap.min.css">
	<link rel="stylesheet" href="../../docs/css/owl.carousel.min.css">
	<link rel="stylesheet" href="../../docs/css/animate.min.css">
	<link id="switch-color" rel="stylesheet" href="../../docs/css/main-red.css">

</head>
<body>

	<!-- Preloader -->
	<div class="preloader">
		<div class="preloader__figure"></div>
	</div>
	<!-- End Preloader -->

	<!-- 404 Section -->
	<div class="page-404">
		<div class="page-404__content">
			<h1>404</h1>
			<div class="page-404__text">
				<p>The page or content you are looking for cannot be found!</p>
				<p>Please search or go back to home.</p>
			</div>
			<a href="index1.py" class="default-button">Home</a>
			<a href="forgetpass.py" class="default-button">Back</a>
		</div>
	</div>
	<!-- End 404 Section -->

	<!-- Style Switcher 
	<div class="color-switcher">
		<a class="picker">
			<i class="zmdi zmdi-invert-colors"></i>
		</a>
		<div class="colors">
			<ul>
				<li><a href="404.html#" id="color-red" class="red">Red</a></li>
				<li><a href="404.html#" id="color-teal" class="teal">Teal</a></li>
				<li><a href="404.html#" id="color-indigo" class="indigo">Indigo</a></li>
				<li><a href="404.html#" id="color-purple" class="purple">Purple</a></li>
				<li><a href="404.html#" id="color-blue-grey" class="blue-grey">Blue Grey</a></li>
				<li><a href="404.html#" id="color-dark" class="dark">Dark</a></li>
			</ul>
		</div>
	</div>
	 End Style Switcher -->

	<!--JS-->
	<script src="../../docs/js/jquery-2.2.4.min.js"></script>
	<script src="../../maps.googleapis.com/maps/api/js.JS"></script>
	<script src="../../docs/js/bootstrap.min.js"></script>
	<script src="../../docs/js/owl.carousel.min.js"></script>
	<script src="../../docs/js/parallax.min.js"></script>
	<script src="../../docs/js/imagesloaded.pkgd.min.js"></script>
	<script src="../../docs/js/main.js"></script>
	</body>
</html>""")
