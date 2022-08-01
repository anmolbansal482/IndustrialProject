#!C:\python27\python.exe
# -*- coding: utf-8 -*-
# import modules from cgi
import changepassfunc

print("Content-type: text/html\n\n")
print("""<!DOCTYPE html>
<html lang="en" class="app">

<head>  
  <meta charset="utf-8" />
    <meta name="description" content="">
	<meta name="keywords" content="">
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
    <div class="container aside-xl">
    <a class="navbar-brand block" href="index1.py">HelpZone</a>
    <a class="navbar-brand block" style="color:#fff;" href="#">Don't want to change.<br> Simmon! go back.</a>
      
      <section class="m-b-lg">
        
          
        
        <form method="post" action="changepass.py">
          <div class="list-group">
            <div class="list-group-item">
              <input type="text" name="oldpass" required placeholder="Old password" class="form-control no-border">""")
changepassfunc.oldp()
print("""</div>
            <div class="list-group-item">
               <input type="text" name="newpass" required placeholder="New Password" class="form-control no-border">
            </div>
            <div class="list-group-item">
               <input type="text" name="confirmpass" required placeholder="Confirm Password" class="form-control no-border">""")
changepassfunc.cpass()
print("""</div>
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Submit</button>
          <div class="text-center m-t m-b"><a href="forgetpass.py"><small>Forgot password?</small></a></div>

        </form>
      </section>
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