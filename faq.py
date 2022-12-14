#!C:\python27\python.exe
# -*- coding: utf-8 -*-
import cgi
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

	<!-- Header -->
	<header class="header">
		<div class="container">
			<div class="row">
				<!-- Logotype -->
				<div class="col-xs-10 col-sm-4">
					<a class="header__logo" href="index.html">
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
								<a id="dropdown-link1" data-target="#" href="faq.html#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Home
								<i class="zmdi zmdi-chevron-down"></i></a>
								<ul class="dropdown-menu" aria-labelledby="dropdown-link1">
									<li>
										<a href="index.html">Home parallax</a>
									</li>
									<li>
										<a href="index-2.html">Home slideshow</a>
									</li>
									<li>
										<a href="index-3.html">Home static</a>
									</li>
								</ul>
							</li>
							<!-- End Dropdown -->

							<!-- Dropdown -->
							<li class="dropdown">
								<a id="dropdown-link2" data-target="#" href="faq.html#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Articles
								<i class="zmdi zmdi-chevron-down"></i></a>
								<ul class="dropdown-menu" aria-labelledby="dropdown-link2">
									<li>
										<a href="articles.html" >Articles default</a>
									</li>
									<li>
										<a href="articles-grid.html">Articles grid</a>
									</li>
								</ul>
							</li>
							<!-- End Dropdown -->

							<li>
								<a href="knowledge.html">Knowledge</a>
							</li>

							<li>
								<a href="faq.html">FAQ</a>
							</li>

							<li>
								<a href="contact.html">Contact</a>
							</li>

							<!-- Dropdown -->
							<li class="dropdown">
								<a id="dropdown-link3" data-target="#" href="faq.html#" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Pages
								<i class="zmdi zmdi-chevron-down"></i></a>
								<ul class="dropdown-menu" aria-labelledby="dropdown-link3">
									<li>
										<a href="about.html">About</a>
									</li>
									<li role="separator" class="divider"></li>
									<li>
										<a href="article.html">Article</a>
									</li>
									<li role="separator" class="divider"></li>
									<li>
										<a href="404.html">404</a>
									</li>
								</ul>
							</li>
							<!-- End Dropdown -->
						</ul>	
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
			<a id="drop1" class="dropdown-toggle" href="faq.html#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Home<i class="zmdi zmdi-chevron-down"></i></a>

			<ul class="dropdown-menu" aria-labelledby="drop1">
				<li>
					<a href="index.html">Home parallax</a>
				</li>
				<li>
					<a href="index-2.html">Home slideshow</a>
				</li>
				<li>
					<a href="index-3.html">Home static</a>
				</li>
			</ul>
		</li>
		<!-- End Dropdown -->

		<!-- Dropdown -->
		<li class="dropdown">
			<a id="drop2" class="dropdown-toggle" href="faq.html#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Articles<i class="zmdi zmdi-chevron-down"></i></a>

			<ul class="dropdown-menu" aria-labelledby="drop2">
				<li><a href="articles.html" >Articles default</a></li>
				<li><a href="articles-grid.html">Articles grid</a></li>
			</ul>
		</li>
		<!-- End Dropdown -->

		<li><a href="knowledge.html">Knowledge</a></li>
		<li><a href="faq.html">FAQ</a></li>
		<li><a href="contact.html">Contact</a></li>
		
		<!-- Dropdown -->
		<li class="dropdown">
			<a id="drop3" class="dropdown-toggle" href="faq.html#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Pages<i class="zmdi zmdi-chevron-down"></i></a>

			<ul class="dropdown-menu" aria-labelledby="drop3">
				<li><a href="about.html">About</a></li>
				<li><a href="article.html">Article</a></li>
				<li><a href="404.html">404</a></li>
			</ul>
		</li>
		<!-- End Dropdown -->
	</ul>
	<!-- End Mobile Navigation -->

	<!-- Headline -->
	<section class="page-title" data-parallax="scroll" data-image-src="img/page-headers/faq_bg.jpg">
		<div class="container">
			<div class="row">
				<div class="col-xs-12">
					<h1>FAQ</h1>
					<p>Answers to your questions</p>
				</div>
			</div>
		</div>
	</section>
	<!-- End Headline -->

	<!-- Section Wrap -->
	<section class="border-bottom">
		<div class="container">
			<div class="row">

				<!-- FAQs List -->
				<div class="col-xs-12 col-md-8 col-lg-9">
					<div class="row">
						<!-- FAQs grid -->
						<div class="card-grid clearfix">
							<!-- FAQ card -->
							<div class="col-xs-12">
								<div class="card faq-card">
									<!-- Title -->
									<h3>What is HelpZone?</h3>
									<!-- End Title -->
									<!-- Text -->
									<p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.</p>
									<!-- End Text -->
								</div>
							</div>
							<!-- End FAQ card -->

							<!-- FAQ card -->
							<div class="col-xs-12">
								<div class="card faq-card">
									<!-- Title -->
									<h3>My page has been blocked!</h3>
									<!-- End Title -->
									<!-- Text -->
									<p>Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
									<!-- End Text -->
								</div>
							</div>
							<!-- End FAQ card -->

							<!-- FAQ card -->
							<div class="col-xs-12">
								<div class="card faq-card">
									<!-- Title -->
									<h3>How to delete my account?</h3>
									<!-- End Title -->
									<!-- Text -->
									<p>But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness.</p>
									<!-- End Text -->
								</div>
							</div>
							<!-- End FAQ card -->
				
							<!-- FAQ card -->
							<div class="col-xs-12">
								<div class="card faq-card">
									<!-- Title -->
									<h3>How do I disable email notifications?</h3>
									<!-- End Title -->
									<!-- Text -->
									<p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet.</p>
									<!-- End Text -->
								</div>
							</div>
							<!-- End FAQ card -->

							<!-- FAQ card -->
							<div class="col-xs-12">
								<div class="card faq-card">
									<!-- Title -->
									<h3>I forgot my password</h3>
									<!-- End Title -->
									<!-- Text -->
									<p>It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</p>
									<!-- End Text -->
								</div>
							</div>
							<!-- End FAQ card -->
						</div>
						<!-- End FAQs grid -->

						<!-- Pagination -->
						<div class="col-xs-12">
							<div class="pagination-wrap">
								<ul class="pagination">
									<li class="disabled">
										<a href="faq.html#" aria-label="Previous">
											<i class="zmdi zmdi-chevron-left"></i>
										</a>
									</li>
									<li class="active"><a href="faq.html#">1</a></li>
									<li><a href="faq.html#">2</a></li>
									<li><a href="faq.html#">3</a></li>
									<li>
										<a href="faq.html#" aria-label="Next">
											<i class="zmdi zmdi-chevron-right"></i>
										</a>
									</li>
								</ul>
							</div>
						</div>
						<!-- End Pagination -->

					</div>
				</div>
				<!-- End FAQs List -->

				<!-- Sidebar -->
				<div class="col-xs-12 col-md-4 col-lg-3 sidebar">
					<div class="row">

						<!-- Popular News -->
						<div class="col-xs-12">
							<div class="widget popular-articles">

								<!-- News -->
								<div class="article-preview">
									<h4><a href="article.html">One of the Stars</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic -->
									<ul class="statistic">
										<li class="likes">
											<a href="faq.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>231</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>421</span>
										</li>
									</ul>
									<!-- End Statistic -->
								</div>
								<!-- End News -->

								<!-- News -->
								<div class="article-preview">
									<h4><a href="article.html">Silken Mist</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic -->
									<ul class="statistic">
										<li class="likes">
											<a href="faq.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>54</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>30</span>
										</li>
									</ul>
									<!-- End Statistic -->
								</div>
								<!-- End News -->

								<!-- News -->
								<div class="article-preview">
									<h4><a href="article.html">Moons</a></h4>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing.</p>
									<!-- Statistic -->
									<ul class="statistic">
										<li class="likes">
											<a href="faq.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
											<span>17</span>
										</li>
										<li class="comments">
											<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
											<span>3</span>
										</li>
									</ul>
									<!-- End Statistic -->
								</div>
								<!-- End News -->
							</div>	
						</div>
						<!-- End Popular News -->

						<!-- Subscribe -->
						<div class="col-xs-12">
							<div class="widget subscribe">
								<h4>Newsletter</h4>
								<form action="faq.html#">
									<div class="form-group">
										<input type="text" placeholder="Email...">
									</div>
									<button type="submit" class="default-button">Subscribe</button>
								</form>
							</div>
						</div>
						<!-- End Subscribe -->
						
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
						<li><a href="faq.html#"><i class="zmdi zmdi-facebook"></i></a></li>
						<li><a href="faq.html#"><i class="zmdi zmdi-twitter"></i></a></li>
						<li><a href="faq.html#"><i class="zmdi zmdi-google-plus"></i></a></li>
						<li><a href="faq.html#"><i class="zmdi zmdi-instagram"></i></a></li>
					</ul>
				</div>
				<!-- End Social links -->

				<!-- Copyright -->
				<div class="col-xs-12 col-sm-6 col-sm-pull-6">
					<div class="footer__copyright">
						<small>Copyright © 2017 <a href="faq.html#">HelpZone</a>. All Rights Reserved.</small>
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

	<!-- Chat -->
	<button type="button" class="chat-button chat-button--fixed">
		<i class="zmdi zmdi-comments"></i>
		<i class="zmdi zmdi-close"></i>
	</button>

	<div class="chat">
		<div class="chat__content">
			
			<!-- Text Wrap -->
			<div class="chat__text-wrap">
				<span class="chat__title">Get support</span>
				<p class="chat__text">Earnest request, before contacting a support check for the answer to your question in our <a href="faq.html">database</a>.</p>
			</div>
			<!-- End Text Wrap -->

			<!-- Correspondence Wrap -->
			<div class="chat__message-wrap">
				<div class="message user clearfix">
					<div class="avatar-wrap">
						<div class="avatar">
							<img src="../../docs/img/user.jpg" alt="">
						</div>
					</div>
					<div class="text-wrap">
						<div class="autor">You</div>
						<div class="time">13:47 am</div>
						<div class="text">
							Hello, I need your help.
						</div>
					</div>
				</div>

				<div class="message adviser clearfix">
					<div class="avatar-wrap">
						<div class="avatar">
							<img src="../../docs/img/user.jpg" alt="">
						</div>
					</div>
					<div class="text-wrap">
						<div class="autor">Adviser</div>
						<div class="time">13:47 am</div>
						<div class="text">
							Hi! We are happy to help you.
						</div>
					</div>
				</div>

				<div class="message user clearfix">
					<div class="avatar-wrap">
						<div class="avatar">
							<img src="../../docs/img/user.jpg" alt="">
						</div>
					</div>
					<div class="text-wrap">
						<div class="autor">You</div>
						<div class="time">13:48 am</div>
						<div class="text">
							Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam eveniet, eos perferendis porro qui, ex placeat officia alias, illo magnam aliquam! Dolore obcaecati possimus, adipisci. Quo eligendi <a href="faq.html#">voluptate</a> iste.
						</div>
					</div>
				</div>

				<div class="message adviser clearfix">
					<div class="avatar-wrap">
						<div class="avatar">
							<img src="../../docs/img/user.jpg" alt="">
						</div>
					</div>
					<div class="text-wrap">
						<div class="autor">Adviser</div>
						<div class="time">13:49 am</div>
						<div class="text">
							Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt impedit, quas tempore ullam. Delectus eaque porro similique <a href="faq.html#">repellendus</a> sint, ipsam.
						</div>
					</div>
				</div>

				<div class="message user clearfix">
					<div class="avatar-wrap">
						<div class="avatar">
							<img src="../../docs/img/user.jpg" alt="">
						</div>
					</div>
					<div class="text-wrap">
						<div class="autor">You</div>
						<div class="time">13:50 am</div>
						<div class="text">
							Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore, dolore.
						</div>
					</div>
				</div>
			</div>
			<!-- End Correspondence Wrap -->

			<!-- Write Message -->
			<form class="chat__write" action="faq.html#">
				<input type="text" placeholder="Write message...">
				<button type="submit" class="default-button"><i class="zmdi zmdi-mail-send"></i></button>
			</form>
			<!-- End Write Message -->

		</div>
	</div>
	<!-- End Chat -->

	<!-- Style Switcher -->
	<div class="color-switcher">
		<a class="picker">
			<i class="zmdi zmdi-invert-colors"></i>
		</a>
		<div class="colors">
			<ul>
				<li><a href="faq.html#" id="color-red" class="red">Red</a></li>
				<li><a href="faq.html#" id="color-teal" class="teal">Teal</a></li>
				<li><a href="faq.html#" id="color-indigo" class="indigo">Indigo</a></li>
				<li><a href="faq.html#" id="color-purple" class="purple">Purple</a></li>
				<li><a href="faq.html#" id="color-blue-grey" class="blue-grey">Blue Grey</a></li>
				<li><a href="faq.html#" id="color-dark" class="dark">Dark</a></li>
			</ul>
		</div>
	</div>
	<!-- End Style Switcher -->

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