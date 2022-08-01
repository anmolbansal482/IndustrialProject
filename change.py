#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
# start signup.py #

import changefunc
print("Content-type: text/html\n\n")
print("""<!DOCTYPE html>
<html lang="en" class="app">

<head>  
  <meta charset="utf-8">
  				<div class="col-xs-10 col-sm-4">


					<a class="header__logo" href="index1.py">
						<img src="../../docs/img/logo.png" alt="">
					</a>
				</div>
  <title>Aid.Me</title>
  <meta name="description" content="app, web app, responsive, admin dashboard, admin, flat, flat ui, ui kit, off screen nav" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" /> 
  <link rel="stylesheet" href="../../docs/changepass/css/bootstrap.css" type="text/css" />
  <link rel="stylesheet" href="../../docs/changepass/css/animate.css" type="text/css" />
  <link rel="stylesheet" href="../../docs/changepass/css/font-awesome.min.css" type="text/css" />
  <link rel="stylesheet" href="../../docs/changepass/css/icon.css" type="text/css" />
  <link rel="stylesheet" href="../../docs/changepass/css/font.css" type="text/css" />
  <link rel="stylesheet" href="../../docs/changepass/css/app.css" type="text/css" />  
    <!--[if lt IE 9]>

    <script src="../../docs/changepass/js/ie/html5shiv.js"></script>
    <script src="../../docs/changepass/js/ie/respond.min.js"></script>
    <script src="../../docs/changepass/js/ie/excanvas.js"></script>
  <![endif]-->
</head>
<body>


  <section id="content" class="m-t-lg wrapper-md animated fadeInUp">    
    <div class="container aside-xl">
    <a class="navbar-brand block" href="user.py">HelpZone</a>""")


changefunc.resetone()
changefunc.resettwo()

print("""</div>
  </section>""")



print("""<footer id="footer">
    <div class="text-center padder">
      <p>
        <small>Copyright &#169; 2017 @Anmol Bansal</a>. All Rights Reserved.</small>
      </p>
    </div>
  </footer>
  <!-- / footer -->
  <script src="../../docs/changepass/js/jquery.min.js"></script>
  <!-- Bootstrap -->
  <script src="../../docs/changepass/js/bootstrap.js"></script>
  <!-- App -->
  <script src="../../docs/changepass/js/app.js"></script>  
  <script src="../../docs/changepass/js/slimscroll/jquery.slimscroll.min.js"></script>
    <script src="../../docs/changepass/js/app.plugin.js"></script>
</body>
</html>""")