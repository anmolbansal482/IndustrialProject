#!C:\python27\python.exe
# -*- coding: utf-8 -*-
# import modules for cgi handling
import govtfunc

print("Content-type:text/html\r\n\r\n")
print("""<!Doctype html>
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
	<link href='https://fonts.googleapis.com/css?family=Roboto:400,500,700%7COpen+Sans:400,600,700' rel='stylesheet' type='text/css'>

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

govtfunc.cookie()

# if 'HTTP_COOKIE' in os.environ:
# cookie_string=os.environ.get('HTTP_COOKIE')
# e1=cookies.SimpleCookie()
# e1load(cookie_string)
# data=e1['shop'].value
##data1=e1['pass'].value
# print("Hi",data)
# else:
# print("Hi,Guest")
# print("Password is",data1)

# a=3
# if (a==10):
# print("sdfjkhsdkf")

# else:
# print("dku")

print("""<ul class="dropdown-menu" aria-labelledby="dropdown-link3"></ul>
							<li class="dropdown">""")

govtfunc.signoutt()
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

					<!-- mobile navigation button -->
					<button type="button" class="header__btn">

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
govtfunc.cookie()
print("""</a></li>""")
print("""<li><a href="signin.py">""")
govtfunc.signoutt()
print("""</a></li>
	</ul>

	<!-- Headline -->
	<section class="page-title" data-parallax="scroll" data-image-src="../../docs/img/other/2802444.jpg">
		<div class="container">
			<div class="row">
				<div class="col-xs-12">
					<h1 style="color:#816b96"></h1>
					<p></p>
				</div>
			</div>
		</div>
	</section>
	<!-- End Headline -->

	<!-- Section Wrap -->
	<section class="border-bottom" data-parallax="scroll" data-image-src="../../docs/img/other/106645.jpg">
		<div class="container">
			<div class="row">

				<!-- Knowledge Base -->
				<div class="col-xs-12 col-md-8 col-lg-9">
					<div class="row">
						<!-- Knowledge grid -->
						<div class="card-grid card-grid--mb clearfix">
							<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">Banking</a></span>
									<ul class="knowledge-card__list">
									    <li class="dropdown">
								            <a id="dropdown-link1" data-target="index-2.py" href="#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">SBI
								            <i class="zmdi zmdi-chevron-down"></i></a>
								            <ul class="dropdown-menu" aria-labelledby="dropdown-link1">
									    <li>
										    <a href="govtsearch.py?search=1">Clerical Cadre</a>
									    </li>
									
									    <li>
										    <a href="govtsearch.py?search=2">Probationary Officer</a>
									    </li>
									
									    <li>
										    <a href="govtsearch.py?search=3">Specialist Officer</a>
									    </li>
									    
				                        </li>
				                           
                                    </ul>
                                    
                                        
									    <li class="dropdown">
								            <a id="dropdown-link1" data-target="index-2.py" href="#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">IBPS
								            <i class="zmdi zmdi-chevron-down"></i></a>
								            <ul class="dropdown-menu" aria-labelledby="dropdown-link1">
									    <li>
										    <a href="govtsearch.py?search=4">Clerical Cadre</a>
									    </li>
									
									    <li>
										    <a href="govtsearch.py?search=5">Probationary Officer</a>
									    </li>
									
									    <li>
										    <a href="govtsearch.py?search=6">Specialist Officer</a>
									    </li>
									    
				                        </li>
		             </div>
						</div>

							<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">SSC</a></span>
									    <ul class="knowledge-card__list">
									    <li class="dropdown">
								            <a href="govtsearch.py?search=7">CHSL
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
				                        <ul>
				                        <li class="dropdown">
								            <a href="govtsearch.py?search=8">CGL</a> 
					                    </li>
				                    </ul>
								</div>
							</div>

                            <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">UPSC</a></span>
									<ul class="knowledge-card__list">
                                        <li class="dropdown">
								            <a href="govtsearch.py?search=9">Indian Administrative Services(IAS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
								        
								        <li class="dropdown">
								            <a href="govtsearch.py?search=10">Indian Police Services(IPS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
								        
								        <li class="dropdown">
								            <a href="govtsearch.py?search=11">Indian Foreign Services(IFS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
								        
								        <li class="dropdown">
								            <a href="govtsearch.py?search=12">Indian Account and Audit Services(IAAS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
								        
								        <li class="dropdown">
								            <a href="govtsearch.py?search=13">Indian Information Services(IIS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
								        
								        <li class="dropdown">
								            <a href="govtsearch.py?search=14">Indian Civil Account Services(ICAS)
								            <i class="zmdi zmdi-chevron-dow"></i></a>
								        </li>
                            </ul>
								</div>
							</div>
                        <!--
							<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">State Exams</a></span>
									<ul class="knowledge-card__list">   
									</ul>
								</div>
							</div> -->
                        <!--
							<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">RBI Exams</a></span>
									<ul class="knowledge-card__list">

                                </ul>
								</div>
							</div> -->
                        <!--
							<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
								<div class="card knowledge-card">
									<span class="knowledge-card__title"><a href="#">Railways</a></span>
									<ul class="knowledge-card__list">

                            </ul>
								</div>
							</div> -->

						</div>
						<!-- End Knowledge grid -->

					</div>
				</div>
				<!-- End Knowledge Base -->

				<!-- Sidebar -->
				<div class="col-xs-12 col-md-4 col-lg-3 sidebar">
					<div class="row">

						<!-- Popular News -->
						<div class="col-xs-12">
							<div class="widget popular-articles">

								<!-- News 
								<div class="article-preview">
									<h4><a href="article.html">One of the Stars</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic 
									<ul class="statistic">
										<li class="likes">
											<a href="knowledge.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>231</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>421</span>
										</li>
									</ul>
									 End Statistic -->
								</div>


								<!-- News
								<div class="article-preview">
									<h4><a href="article.html">Silken Mist</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic 
									<ul class="statistic">
										<li class="likes">
											<a href="knowledge.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>54</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>30</span>
										</li>
									</ul>
									 End Statistic -->
								</div>


								<!-- News
								<div class="article-preview">
									<h4><a href="article.html">Moons</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic 
									<ul class="statistic">
										<li class="likes">
											<a href="knowledge.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>17</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>3</span>
										</li>
									</ul>
									End Statistic -->
								</div>
								<!-- End News -->
							</div>	
						</div>
						<!-- End Popular News -->


					</div>
				</div>
				<!-- End Sidebar -->

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
						<li><a href="https://www.facebook.com/sunny.rapper"><i class="zmdi zmdi-facebook"></i></a></li>
						<li><a href="https://twitter.com/AnmolBa12915536"><i class="zmdi zmdi-twitter"></i></a></li>
						<li><a href="http://www.gmail.com"><i class="zmdi zmdi-google-plus"></i></a></li>
						<li><a href="knowledge.html#"><i class="zmdi zmdi-instagram"></i></a></li>
					</ul>
				</div>
				<!-- End Social links -->

				<!-- Copyright -->
				<div class="col-xs-12 col-sm-6 col-sm-pull-6">
					<div class="footer__copyright">
						<small>Copyright © 2017 <a href="knowledge.html#">Anmol Bansal</a>. All Rights Reserved.</small>
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
				<li><a href="knowledge.html#" id="color-red" class="red">Red</a></li>
				<li><a href="knowledge.html#" id="color-teal" class="teal">Teal</a></li>
				<li><a href="knowledge.html#" id="color-indigo" class="indigo">Indigo</a></li>
				<li><a href="knowledge.html#" id="color-purple" class="purple">Purple</a></li>
				<li><a href="knowledge.html#" id="color-blue-grey" class="blue-grey">Blue Grey</a></li>
				<li><a href="knowledge.html#" id="color-dark" class="dark">Dark</a></li>
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