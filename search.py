#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules from cgi
import searchengine
import cgitb; cgitb.enable()

print ("Content-type: text/html\n\n")

print ("""<!Doctype html>
<html lang="en">
<head>
	<title>HelpZone</title>
	<meta name="description" content="">
	<meta name="keywords" content="">
	<meta charset="utf-8">
	<meta name="author" content="Anmol Bansal">
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

	<!-- Header -->
	<header class="header">
		<div class="container">
			<div class="row">
			
				<!-- Logotype -->
				<div class="col-xs-10 col-sm-4">
				<a class="header__logo" href="index1.py">
						<img src="../../docs/img/logo.png" alt="">
					</a>
				</div>
				<!-- End Logotype -->

				<!-- Navigation -->
				<div class="col-xs-2 col-sm-8">
					<nav class="header__nav-wrap">
						<ul class="header__nav">
							<!-- Dropdown -->
							<li class="dropdown">
								<a id="dropdown-link1" data-target="" href="index1.py" data-toggle="" role="button" aria-haspopup="true" aria-expanded="false">Home

								<ul class="dropdown-menu" aria-labelledby="dropdown-link1">


								</ul>
							</li>
							<!-- End Dropdown -->

							<!-- Dropdown -->
							<li class="dropdown">
								<a id="dropdown-link2" data-target="index-2.py" href="top-unis.py" data-toggle="" role="button" aria-haspopup="true" aria-expanded="false">Top Univesities

								<ul class="dropdown-menu" aria-labelledby="dropdown-link2">

								</ul>
							</li>
							<!-- End Dropdown -->

							<li>
								<a href="govt.py">Govt. Exams</a>
							</li>

							<!--<li>
								<a href="faq.py">FAQ</a>
							</li>-->

							<li>
								<a href="contact.py">Contact</a>
							</li>

							<!-- Dropdown -->
							<li class="dropdown">
								<a id="dropdown-link3" data-target="#" href="index-2.py" data-toggle="dropdown"
								 role="button" aria-haspopup="true" aria-expanded="false">""")

searchengine.cookie()

#if 'HTTP_COOKIE' in os.environ:
    #cookie_string=os.environ.get('HTTP_COOKIE')
    #e1=cookies.SimpleCookie()
    #e1load(cookie_string)
    #data=e1['shop'].value
    ##data1=e1['pass'].value
    #print("Hi",data)
#else:
    #print("Hi,Guest")
#print("Password is",data1)

#a=3
#if (a==10):
	#print("sdfjkhsdkf")

#else:
	#print("dku")

print("""<ul class="dropdown-menu" aria-labelledby="dropdown-link3"></ul>
							<li class="dropdown">""")


searchengine.signoutt()
print("""<ul class="dropdown-menu" aria-labelledby="dropdown-link2">

								</ul>
							</li>
							<!-- End Dropdown -->
						</ul>
						</li>
					</nav>

					<!-- mobile navigation button -->
					<button type="button" class="header__btn">
						<i class="zmdi zmdi-menu"></i>
						<i class="zmdi zmdi-close"></i>
					</button>
					<!-- end mobile navigation button -->
				</div>
				<!-- End Navigation -->
			</div>
		</div>
	</header>
	<!-- End Header -->

	
	<!-- Mobile Navigation -->
	<ul class="mobile-navigation">
		<!-- Dropdown -->
		<li class="dropdown">
			<a id="drop1" class="dropdown-toggle" href="index1.py" data-toggle="" aria-haspopup="true" aria-expanded="false">Home</a>

			<ul class="dropdown-menu" aria-labelledby="drop1">

			</ul>
		</li>
		<!-- End Dropdown -->

		<!-- Dropdown -->
		<li class="dropdown">
			<a id="drop2" class="dropdown-toggle" href="top-unis.py" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Top Universities</a>
            </li>
		<!-- End Dropdown -->

		<li><a href="govt.py">Govt. Exams</a></li>
		<li><a href="contact.py">Contact</a></li>
		<li><a href="User.py">""")
searchengine.cookie()
print("""</a></li>""")
print("""<li><a href="signin.py">""")
searchengine.signoutt()
print("""</a></li>
	</ul>
<!-- Headline -->
	<section class="page-title" data-parallax="scroll" data-image-src="../../docs/img/articles/article1_2.jpg">
		<div class="container">
                        <div class="row">
                        <div class="col-xs-12">

<h1></h1>
					
				</div>
			</div>
		</div>
	</section>
	<!-- End Headline -->

	<!-- Section Wrap -->
	<section class="border-bottom">
	

		<!-- Filter  
		<div class="filter">
			<div class="container">
				<div class="row">

					<!-- Search 
					<div class="col-xs-12 col-sm-4 col-md-3">
						<form class="filter__search" action="articles-grid.html#">
							<input type="text" placeholder="Search university...">
							<button type="submit"><i class="zmdi zmdi-search"></i></button>
						</form>
					</div>
					 End Search -->

					<!-- Sort  
					<div class="col-xs-12 col-sm-8 col-md-9">
						<ul class="sort">
							<li>Sort:</li>
							<li><a class="active" href="articles-grid.html#">All</a></li>
							<li><a href="articles-grid.html#">Recent</a></li>
							<li><a href="articles-grid.html#">Popular</a></li>
						</ul>
					</div>
					 End Sort -->

				</div>
			</div>
		</div>
		 
		 
<div class="container">""")
searchengine.article()
searchengine.univ()
searchengine.gov()
		
print("""<div class="row">
			<!-- Article List -->
				<div class="col-xs-12 col-md-8 col-lg-9">
					<div class="row">

						<!-- Articles grid -->
						<div class="card-grid clearfix">
							</div>
		</div>
    </section>
	<!-- End Section Wrap -->

	<!-- Footer -->
	<footer class="footer">
		<div class="container">
			<div class="row">
				<!-- Social links -->
				<div class="col-xs-12 col-sm-6 col-sm-push-6">
					<ul class="footer__social-list">
						<li><a href="articles-grid.html#"><i class="zmdi zmdi-facebook"></i></a></li>
						<li><a href="articles-grid.html#"><i class="zmdi zmdi-twitter"></i></a></li>
						<li><a href="articles-grid.html#"><i class="zmdi zmdi-google-plus"></i></a></li>
						<li><a href="articles-grid.html#"><i class="zmdi zmdi-instagram"></i></a></li>
					</ul>
				</div>
				<!-- End Social links -->

				<!-- Copyright -->
				<div class="col-xs-12 col-sm-6 col-sm-pull-6">
					<div class="footer__copyright">
						<small>Copyright © 2017 <a href="articles-grid.html#">Anmol Bansal</a>. All Rights Reserved.</small>
					</div>
				</div>
				<!-- End Copyright -->

				<!-- Back to top -->
				<button type="button" class="footer__btn"><i class="zmdi zmdi-chevron-up"></i></button>
				<!-- End Back to top -->
			</div>
		</div>
	</footer>
	<!-- End Footer -->

	
	<!-- Style Switcher
	<div class="color-switcher">
		<a class="picker">
			<i class="zmdi zmdi-invert-colors"></i>
		</a>
		<div class="colors">
			<ul>
				<li><a href="articles-grid.html#" id="color-red" class="red">Red</a></li>
				<li><a href="articles-grid.html#" id="color-teal" class="teal">Teal</a></li>
				<li><a href="articles-grid.html#" id="color-indigo" class="indigo">Indigo</a></li>
				<li><a href="articles-grid.html#" id="color-purple" class="purple">Purple</a></li>
				<li><a href="articles-grid.html#" id="color-blue-grey" class="blue-grey">Blue Grey</a></li>
				<li><a href="articles-grid.html#" id="color-dark" class="dark">Dark</a></li>
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