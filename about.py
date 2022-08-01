#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import cgi
import index1func
import sqlite3
print ("Content-type:text/html\r\n\r\n")
print ("""<!Doctype html>
<html lang="en">
<head>
	<title>HelpZone</title>
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
								<a id="dropdown-link3" data-target="#" href="index-2.py" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">""")


index1func.cookie()

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

index1func.signoutt()

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
index1func.cookie()
print("""</a></li>""")
print("""<li><a href="signin.py">""")
index1func.signoutt()
print("""</a></li>
	</ul>
	<!-- Headline -->
	<section class="page-title" data-parallax="scroll" data-image-src="../../docs/img/other/about-us.jpg">
		<div class="container">
			<div class="row">
				<div class="col-xs-12">
					
				</div>
			</div>
		</div>
	</section>
	<!-- End Headline -->

	<!-- About Section -->
	<section class="section-padding-70 white-bg border-bottom">
		<div class="container">
			<div class="row">
				<!-- About text -->
				<div class="col-xs-12 col-md-5 col-md-push-7 col-lg-push-6 col-lg-6">
					<h2>What we do</h2>
					<p>We Provide information to every age group related to their career and universities they can look for depending upon their budget, interests and desitred location. It is available for school students, college students and for Ph.D desiring candidates as well.</p>
					<p>Apart from that we also make people aware about government exams such as Banking, UPSC, State exams etc. Through our website, people will be able to look for multiple informations on a single platform only. Be it the student o engineering, law, medical etc. or a government job aspirant.</p>
				</div>
				<!-- End About text -->

				<!-- Img -->
				<div class="col-xs-12 col-md-7 col-md-pull-5 col-lg-pull-6 col-lg-6">
					<div class="owl-carousel owl-theme img-carousel">

						<!-- Slide -->
						<div class="item">
							<img src="../../docs/img/other/img-slide-1.jpg" alt="">
						</div>
						<!-- End Slide -->

						<!-- Slide -->
						<div class="item">
							<img src="../../docs/img/other/img-slide-2.jpg" alt="">
						</div>
						<!-- End Slide -->

						<!-- Slide -->
						<div class="item">
							<img src="../../docs/img/other/img-slide-3.jpg" alt="">
						</div>
						<!-- End Slide -->
							
					</div>
				</div>
				<!-- End Img -->
			</div>
		</div>
	</section>
	<!-- End About Section -->



	<!-- Footer -->
	<footer class="footer">
		<div class="container">
			<div class="row">
				<!-- Social links -->
				<div class="col-xs-12 col-sm-6 col-sm-push-6">
					<ul class="footer__social-list">
						<li><a href="https://www.facebook.com/sunny.rapper"><i class="zmdi zmdi-facebook"></i></a></li>
						<li><a href="https://twitter.com/AnmolBa12915536"><i class="zmdi zmdi-twitter"></i></a></li>
						<li><a href="https://gmail.com"><i class="zmdi zmdi-google-plus"></i></a></li>
						<li><a href="about.html#"><i class="zmdi zmdi-instagram"></i></a></li>
					</ul>
				</div>
				<!-- End Social links -->

				<!-- Copyright -->
				<div class="col-xs-12 col-sm-6 col-sm-pull-6">
					<div class="footer__copyright">
						<small>Copyright © 2017 <a href="about.html#">HelpZone</a>. All Rights Reserved.</small>
					</div>
				</div>
				<!-- End Copyright -->

			</div>
		</div>
	</footer>
	<!-- End Footer -->

	

			<!-- Write Message 
			<form class="chat__write" action="about.html#">
				<input type="text" placeholder="Write message...">
				<button type="submit" class="default-button"><i class="zmdi zmdi-mail-send"></i></button>
			</form>
			 End Write Message -->

		</div>
	</div>
	 

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