#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling

import signinfunc

print ("Content-type:text/html\r\n\r\n")
print ("""<!DOCTYPE html>""")
signinfunc.sign()
print("""<html lang="en">
<head>
	<title>Sign In</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->
	<link rel="icon" type="image/png" href="../../docs/img/logo login/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/icon-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/animate.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/select2.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/util.css">
	<link rel="stylesheet" type="text/css" href="../../docs/css/signin/main.css">
<!--===============================================================================================-->
</head>
<body>

	<div class="limiter">
		<div class="container-login100" style="background-image: url('../../docs/img/other/abstract-autumn-autumn-colours-688830.jpg');">
			<!-- <div class="wrap-login100 p-l-110 p-r-110 p-t-62 p-b-33"> -->
				<form class="login100-form validate-form flex-sb flex-w" method="post" action=""> <!-- it was login-form2.py before -->
					<span class="login100-form-title p-b-53" Style="color:#000;">
						Welcome to Helpzone 
						
					</span>
					<!-- facebook and google icons
					<a href="https://www.facebook.com" class="btn-face m-b-20">
						<img src="../../docs/img/logo login/if_square-facebook_317727 (1).png" alt="FACEBOOK">
						Facebook
					</a>

					<a href="https://www.gmail.com" class="btn-google m-b-20">
						<img src="../../docs/img/logo login/icon-google.png" alt="GOOGLE">
						Google
					</a>
					-->
					<div style="margin-left:500px;">
					<div class="p-t-31 p-b-9">
						<span class="txt1" Style="color:#000; margin-top:10px; text:align:center;">
							<h4 style="margin-left:110px;">Username</h4>
						</span>
					
					
					<div class="wrap-input100 validate-input" data-validate = "Username is required">
						<input class="input100" type="text" name="username" >
						<span class="focus-input100"></span>
					</div>
					</div>
                    </div>
                    
                    <div style="margin-left:500px;">
					<div class="p-t-13 p-b-9 ">
						<span class="txt1" Style="color:#000;">
							<h4 style="margin-left:110px;">Password</h4>
						</span>
						
						
					</div>
					 
						
					<div class="wrap-input100 validate-input"  data-validate = "Password is required">
						<input class="input100" type="password" name="pwd" >
						<span class="focus-input100"></span>
					</div>
					<a href="forgetpass.py" class="txt2 bo1 m-l-5">
							Forgot?
						</a> 
					</div>""")
signinfunc.flago()
print("""<div class="container-login100-form-btn m-t-17" style="margin-left:530px;">
						<button class="login100-form-btn">
						<a href="" class="txt2 bo1">
							<h5 Style="color:#fff;">Sign In</h5>
						</button>
					</div>

					<div class="w-full text-center p-t-55">
						<span class="txt2" style="color:#fff;">
							Not a member?
						</span><br><br>
						<div class="container-login100-form-btn m-t-17" style="margin-left:530px;">
						
						<button class="login100-form-btn" style="color:#070408;">
							<h5 style="color:#fff;"><a href="signup.py" class="txt2 bo1" Style="color:#fff;">
						 Sign up now</a></h5>
						</button>
					</div>
					</div>
				</form>

			</div>
		</div>
	</div>


	<div id="dropDownSelect1"></div>

<!--===============================================================================================-->
	<script src="../../docs/js/signin/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/popper.js"></script>
	<script src="../../docs/js/signin/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/moment.min.js"></script>
	<script src="../../docs/js/signin/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="../../docs/js/signin/main.js"></script>
	
</body>
</html>""")
