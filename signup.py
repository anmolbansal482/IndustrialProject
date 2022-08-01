#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling

import signupfunc

print ("Content-type: text/html\n\n")
print ("""<!Doctype html>""")

signupfunc.sign()

print("""<html lang="en">
<head>
	<title>Sign Up</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="../../docs/img/logo login/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/icon-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/material-design-iconic-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/util.css">
	<link rel="stylesheet" type="text/css" href="../../docs/css/login/main.css">
<!--===============================================================================================-->
</head>
<body style="background-color: #070408;">

	<div class="limiter">
		<div class="container-login100">
			<div class="login100-more" style="background-image: url('../../docs/img/other/Anime-Motivational-backgrounds.jpg');"></div>

			<div class="wrap-login100 p-l-50 p-r-50 p-t-72 p-b-50">
				<form class="login100-form validate-form" method="post" action="">
					<span class="login100-form-title p-b-59">
						Welcome to Helpzone
					</span>

					<div class="wrap-input100 validate-input" data-validate="Name is required">
						<span class="label-input100" style="color:#070408;">Full Name</span>
						<input class="input100" type="text" name="name" placeholder="Name...">
						<span class="focus-input100"></span>
					</div>""")

print("""<div class="wrap-input100 validate-input" data-validate="Username is required">
						<span class="label-input100" style="color:#070408;">Username</span>
						<input class="input100" type="text" name="username" placeholder="Username...">
						<span class="focus-input100"></span>
						</div>""")
signupfunc.uname()


print("""<div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
						<span class="label-input100" style="color:#070408;">Email</span>
						<input class="input100" type="text" name="email" placeholder="Email addess...">
						<span class="focus-input100"></span>
						</div>""")
signupfunc.mail()
print("""<div class="wrap-input100 validate-input" data-validate = "Password is required">
						<span class="label-input100" style="color:#070408;">Password</span>
						<input class="input100" type="password" name="pass" placeholder="*************">
						<span class="focus-input100"></span>
					</div>

					<div class="wrap-input100 validate-input" data-validate = "Repeat Password is required">
						<span class="label-input100" style="color:#070408;">Confirm Password</span>
						<input class="input100" type="password" name="repeat-pass" placeholder="*************">
						<span class="focus-input100"></span>
					</div>""")
signupfunc.confirmpass()
print("""<div class="flex-m w-full p-b-33">
						<div class="contact100-form-checkbox">
						</div>


					</div>

					<div class="container-login100-form-btn">
						<div class="wrap-login100-form-btn">
							<div class="login100-form-bgbtn"></div>
							<button class="login100-form-btn" style="color:#fff;">
								Sign Up
							</button>
						</div>

						<a href="signin.py" class="dis-block txt3 hov1 p-r-30 p-t-10 p-b-10 p-l-30">
							OR Sign In
							<!-- icon
							<i class="fa fa-long-arrow-right m-l-5"></i>
							icon -->
						</a>

					</div>
				</form>
			</div>
		</div>
	</div>


<!--===============================================================================================-->
	<script src="../../docs/js/login/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/popper.js"></script>
	<script src="../../docs/js/login/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/moment.min.js"></script>
	<script src="../../docs/js/login/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/login/main.js"></script>
	
</body>
</html>""")
signupfunc.create()