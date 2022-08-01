#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
import index1func

print ("Content-type: text/html\n\n")

print ("""<!Doctype html>
<html lang="en">
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
	
	<!-- Home Section -->
	<section class="home home--slider">

		<!-- Slider -->
		<div class="owl-carousel owl-theme home-carousel">
			<!-- Slide -->
			<div class="item slideshow-item" data-bg="../../docs/img/other/books-library-students-12064.jpg">
			</div>
			<!-- End Slide -->

			<!-- Slide -->
			<div class="item slideshow-item" data-bg="../../docs/img/other/conceptual-creativity-cube-327186.jpg">
			</div>
			<!-- End Slide -->

			<!-- Slide -->
			<div class="item slideshow-item" data-bg="../../docs/img/other/pexels-photo-317355.jpeg">
			</div>
			<!-- End Slide -->
		</div>
		<!-- End Slider -->

		<div class="col-xs-12 col-md-8 col-md-offset-2 home__title">
			<div class="home__text-wrap">
				<!-- Title -->
				<h1>Start with a Dream. Finish With a Future</h1>
				<h5 style="color:#fff">Find articles, help, and advice for getting the most for your career.</h5>
				<!-- End Title -->
				<div class="home__search">
					<form method="post" id="say" action="search.py" class="home__search">
						<input type="text" name="search" id="transcript" autofocus="autofocus" placeholder="Dreamers Start here" style="border:none; border-bottom:solid 1px;"/><br>
						<img style="float:right;" onclick="startDictation()" src="../../docs/img/other/if_mic_1055024.png"/>
						<button type="submit" name="search"><i class="zmdi zmdi-search"></i></button>
				    </form>
<script>

function startDictation() {

if (window.hasOwnProperty('webkitSpeechRecognition')) {

var recognition = new webkitSpeechRecognition();

recognition.continuous = false;

recognition.interimResults = false;

recognition.lang = "en-US";

recognition.start();

recognition.onresult = function(e) {

document.getElementById('transcript').value

= e.results[0][0].transcript;

recognition.stop();

document.getElementById('say').submit();

};

recognition.onerror = function(e) {

recognition.stop();

}

}

}

</script><br><br>

<script>
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}
</script>
</head>

<body style="color:#ffffff;" onload="startTime()">

<div id="txt"></div>

</body>
                    </form>
				</div>
			</div>
		</div>
		
	</section>
	<!-- End Home Section -->
	<!-- Filter 
		<div class="filter">
			<div class="container">
				<div class="row" style="">

					<!-- Search 
					<div class="col-xs-12 col-sm-4 col-md-3" >
						<form class="filter__search" action="top-unis.py">
							<input type="text" placeholder="Search University...">
							<button type="submit"><i class="zmdi zmdi-search"></i></button>
						</form>
					</div>
					 End Search -->

					<!-- Sort
					<div class="col-xs-12 col-sm-8 col-md-9">
						<ul class="sort">
							<li>Sort :</li>
							<li><a class="active" href="articles-grid.html#">All</a></li>
							<li><a href="articles-grid.html#">Recent</a></li>
							<li><a href="articles-grid.html#">Popular</a></li>
						</ul>
					</div>
					 End Sort -->

				</div>
			</div>
		</div>
		
<!-- Articles Section -->
	<section class="section-padding-100 border-bottom">

		<div class="container">
			<div class="row">

				<!-- Section title -->
				<div class="col-xs-12">
					<div class="section-title">
						<h2 style="color:white">Latest articles</h2>
						<p style="color:white">Our articles most useful</p>
					</div>
				</div>
				<!-- End Section title -->

				<!-- Article card -->
				<div class="col-xs-12 col-md-8 col-lg-6">
					<div class="card article-card">
						<div class="card-wrap">
							<a href="https://www.studyinnorway.no/"></a>
							<!-- Background card -->
							<img src="../../docs/img/articles/norway-flag.jpg" alt="">
							<!-- End Background card -->
							<!-- Article category -->
							<div class="category category--pink"></div>
							<!-- End Article category -->
							<h3>How to Apply to an International University in Norway in 2018</h3>
							<p>Norway! Home of the paperclip, IKEA names for wardrobes and hall furniture and a knighted penguin. With such quirky people, how could you not want to study here?
                             Fortunately, international students do wish to study here; the Northern-European country welcoming more than 25.000 such pupils on its cold lands.  </p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.py"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.py#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card -->

				<!-- Article card (white background) -->
				<div class="col-xs-12 col-md-4 col-lg-3">
					<div class="card article-card article-card--white">
						<div class="card-wrap">
							<a href="#"></a>
							<!-- Article category -->
							<span class="category category--purple"></span>
							<!-- End Article category -->
							<h3>Maximize efficiency</h3>
							<p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.py"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.py#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							 End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card (white background) -->

				<!-- Article card (white background) -->
				<div class="col-xs-12 col-md-4 col-lg-3">
					<div class="card article-card article-card--white">
						<div class="card-wrap">
							<a href="#"></a>
							<!-- Article category -->
							<span class="category category--orange"></span>
							<!-- End Article category -->
							<h3>Impact</h3>
							<p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.</p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							 End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card (white background) -->

				<!-- Article card (white background) -->
				<div class="col-xs-12 col-md-8 col-lg-3">
					<div class="card article-card article-card--white">
						<div class="card-wrap">
							<a href="https://www.4icu.org/in/himachal-pradesh/"></a>
							<!-- Article category -->
							<span class="category category--teal"></span>
							<!-- End Article category -->
							<h3>Top UNiversitites in Himachal Pradesh</h3>
							<p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card (white background) -->

				<!-- Article card -->
				<div class="col-xs-12 col-md-8 col-lg-6">
					<div class="card article-card">
						<div class="card-wrap">
							<a href="#"></a>
							<!-- Background card -->
							<img src="../../docs/img/articles/es-cheap-destinations-compnew.jpg" alt="">
							<!-- End Background card -->
							<!-- Article category -->
							<span class="category category--indigo"></span>
							<!-- End Article category -->
							<h3>7 Affordable EU Countries to Study a Master's Abroad in 2018</h3>
							<p>Getting a higher education abroad is a great accomplishment and a life-changing experience, but most times it also involves high costs. What if you could erase the high costs factor, though? You will find the ideal destination abroad, where you can pursue your Master’s degree and benefit from low tuition and overall low living costs.</p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							 End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card -->

				<!-- Article card (white background) -->
				<div class="col-xs-12 col-md-4 col-lg-3">
					<div class="card article-card article-card--white">
						<div class="card-wrap">
							<a href="#"></a>
							<!-- Article category -->
							<span class="category category--red"></span>
							<!-- End Article category -->
							<h3>HelpZone</h3>
							<p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.</p>
							<!-- Statistic
							<ul class="statistic">
								<li class="likes">
									<a href="index-2.html#"><i class="zmdi zmdi-favorite-outline"></i></a>
									<span>231</span>
								</li>
								<li class="comments">
									<a href="article.html#comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
									<span>421</span>
								</li>
							</ul>
							End Statistic -->
						</div>
					</div>
				</div>
				<!-- End Article card (white background) -->

				
			</div>
		</div>
	</section>
	<!-- End Articles Section -->

                <!-- FAQ card -->
                <section class="section-padding-101 border-bottom">

		        <div class="container">
			    <div class="row">

                
				<div class="col-xs-12 col-md-6 col-lg-3">
					<div class="card faq-card">
					
						<!-- Title -->
						<h3 style="color:#000;"><a href="forgetpass.py">I forgot my password</a></h3>
						<!-- End Title -->
						<!-- Text -->
						<p>We are here to help you in case your forgot your password. Just click on me and you are good to go to reset your password.</p>
						<!-- End Text -->
					</div>
				</div>
				<!-- End FAQ card -->

				<!-- FAQ card -->
				<div class="col-xs-12 col-md-6 col-lg-3">
					<div class="card faq-card">
						<!-- Title -->
						<h3 style="color:#000;"><a href="contact.py">How to send Queries !</a></h3>
						<!-- End Title -->
						<!-- Text -->
						<p>What if I face a problem on it and I need to contact someone to solve that query. So, in order to contact the HelpZone, how should I contact.</p>
						<!-- End Text -->
					</div>
				</div>
				<!-- End FAQ card -->

				<!-- FAQ card -->
				<div class="col-xs-12 col-md-6 col-lg-3">
					<div class="card faq-card">
						<!-- Title -->
						<h3 style="color:#000;"><a href="changepass.py">How to change password !</a></h3>
						<!-- End Title -->
						<!-- Text -->
						<p>Once one has send a password and it might require to change it all over again, so here's what you can do. Click on me and change your password now.</p>
						<!-- End Text -->
					</div>
				</div>
				<!-- End FAQ card -->

				<!-- FAQ card -->
				<div class="col-xs-12 col-md-6 col-lg-3">
					<div class="card faq-card">
						<!-- Title -->
						<h3 style="color:#000;"><a href="map.py">How to change location !</a></h3>
						<!-- End Title -->
						<!-- Text -->
						<p>Click here and update your location for best results.</p>
						<!-- End Text -->
					</div>
				</div>
				<!-- End FAQ card 
				<!-- View all -->
				<div class="col-xs-12">
					<div class="view-all">
						<a href="about.py" class="default-button">About Us</a>
					</div>
				</div>
				 <!-- End View all -->

			</div>
		</div>
		</div>
		</div>
	</section>
	<!-- End FAQs Section -->


	
	<footer class="footer">
		<div class="container">
			<div class="row">
				
				<div class="col-xs-12 col-sm-6 col-sm-push-6">
					<ul class="footer__social-list">
						<li><a href="https://www.facebook.com/sunny.rapper"><i class="zmdi zmdi-facebook"></i></a></li>
						<li><a href="https://twitter.com/AnmolBa12915536"><i class="zmdi zmdi-twitter"></i></a></li>
						<li><a href="http://www.gmail.com"><i class="zmdi zmdi-google-plus"></i></a></li>
						<!-- <li><a href="index-2.html#"><i class="zmdi zmdi-instagram"></i></a></li> -->
					</ul>
				</div>
			     

				
				<div class="col-xs-12 col-sm-6 col-sm-pull-6">
					<div class="footer__copyright">
						<small>Copyright &#x24B8; 2017 <a href="index-2.html#">Anmol Bansal.</a> All Rights Reserved.</small>
					</div>
				</div>
				 


			</div>
		</div>
	</footer>
    

	


	<!--JS-->
	<script src="http://localhost/docs/js/jquery-2.2.4.min.js"></script>
	
	<script src="http://localhost/docs/js/bootstrap.min.js"></script>
	<script src="http://localhost/docs/js/owl.carousel.min.js"></script>
	<script src="http://localhost/docs/js/parallax.min.js"></script>
	<script src="http://localhost/docs/js/imagesloaded.pkgd.min.js"></script>
	<script src="http://localhost/docs/js/main.js"></script>
	</body>
</html>""")
