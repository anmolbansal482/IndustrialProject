#!C:\python27\python.exe
# -*- coding: utf-8 -*-
# import modules from cgi
import forgetfunc

print("Content-type: text/html\n\n")
print("""<!DOCTYPE html>
<html lang="en" class="app">

<head>  
   <meta charset="utf-8" />
    <meta name="description" content="">
	<meta name="keywords" content="">
	<meta charset="utf-8">
	<meta name="author" content="Dmitry Volkov">
	<!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1"><![endif]-->
	<meta name="viewport" content="width=device-width, initial-scale=1">

  <title>HelpZone</title>
 <link rel="icon" type="image/png" href="../../docs/icon/favicon-16x16.png" sizes="16x16">
	<link rel="icon" type="image/png" href="../../docs/icon/favicon-32x32.png" sizes="32x32">
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
    <div class="container aside-xl"><br><br>
    <a class="navbar-brand block" href="404.py"><h1 style='color:#fff;'>HelpZone</h1></a><br><br>
    <a class="navbar-brand block"><h3 style='color:#fff;'>Please enter your email to reset your password.</h3></a><br><br><br><br>
    
    <form method="post" action="">
          <div class="list-group">
            <div class="list-group-item">
              <input type="text" name="emailchange" required placeholder="Enter your email..." class="form-control no-border">
            </div>
        <button type="submit" class="btn btn-lg btn-primary btn-block">RESET</button>""")
forgetfunc.smail()
print("""</form>
     
    </div>
  </section>
  <!-- footer -->
  <footer id="footer">
    <div class="text-center padder">
      <p>
        <small style="color:#fff;">Copyright &#169; 2017 @Anmol Bansal</a>. All Rights Reserved.</small>
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