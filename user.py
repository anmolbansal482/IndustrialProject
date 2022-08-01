#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
import profilefunc
print ("Content-type:text/html\r\n\r\n")
print("""<!DOCTYPE html>
<html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="../../docs/icon/favicon-16x16.png" sizes="16x16">
	<link rel="icon" type="image/png" href="../../docs/icon/favicon-32x32.png" sizes="32x32">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <title>HelpZone</title>
    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
    <!--     Fonts and icons     -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200" rel="stylesheet" />
    <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
    <!-- CSS Files -->
    <link href="../../docs/profile/assets/css/bootstrap.min.css" rel="stylesheet" />
    <link href="../../docs/profile/assets/css/now-ui-dashboard.css?v=1.0.1" rel="stylesheet" />
    <!-- CSS Just for demo purpose, don't include it in your project -->
    <link href="../../docs/profile/assets/demo/demo.css" rel="stylesheet" />
</head>

<body class="">
    <div class="wrapper ">
        <div class="sidebar" data-color="red">
            <!--
        Tip 1: You can change the color of the sidebar using: data-color="blue | green | orange | red | yellow"
            -->
            <div class="logo">
                
                <a href="index1.py" class="simple-text logo-normal">
                    Helpzone
                </a>
            </div>
            <div class="sidebar-wrapper">
                <ul class="nav">
                    <!-- <li>
                        <a href="dashboard.py">
                            <i class="now-ui-icons design_app"></i>
                            <p>Dashboard</p>
                        </a>
                    </li> -->
                    <!-- <li>
                        <a href="icons.py">
                            <i class="now-ui-icons education_atom"></i>
                            <p>Icons</p>
                        </a>
                    </li> -->
                    
                    <li class="active">
                        <a href="user.py">
                            <i class="now-ui-icons users_single-02"></i>
                            <p>User Profile</p>
                        </a>
                    </li>
                    <li>
                        <a href="map.py">
                            <i class="now-ui-icons location_map-big"></i>
                            <p>Maps</p>
                        </a>
                    </li>
                    <!-- <li>
                        <a href="notifications.py">
                            <i class="now-ui-icons ui-1_bell-53"></i>
                            <p>Notifications</p>
                        </a>
                    </li> -->
                    <li class="notifications">
                        <a href="changepass.py">
                            <i class="now-ui-icons users_single-02"></i>
                            <p>Change Password</p>
                        </a>
                    </li>
                   <li class="notifications"> 
                        <a href="adddata.py">
                            <i class="now-ui-icons design_bullet-list-67"></i>
                            <p>Add data</p>
                        </a>
                     </li> 
                    <!-- <li>
                        <a href="typography.py">
                            <i class="now-ui-icons text_caps-small"></i>
                            <p>Typography</p>
                        </a>
                    </li> -->
                    <!-- <li class="active-pro">
                        <a href="upgrade.py">
                            <i class="now-ui-icons arrows-1_cloud-download-93"></i>
                            <p>Upgrade to PRO</p>
                        </a>
                    </li> -->
                </ul>
            </div>
        </div>
        <div class="main-panel">
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg navbar-transparent  navbar-absolute bg-primary fixed-top">
                <div class="container-fluid">
                    <div class="navbar-wrapper">
                        <div class="navbar-toggle">
                            <button type="button" class="navbar-toggler">
                                <span class="navbar-toggler-bar bar1"></span>
                                <span class="navbar-toggler-bar bar2"></span>
                                <span class="navbar-toggler-bar bar3"></span>
                            </button>
                        </div>
                        <a class="navbar-brand" href="#pablo"></a>
                    </div>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navigation" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-bar navbar-kebab"></span>
                        <span class="navbar-toggler-bar navbar-kebab"></span>
                        <span class="navbar-toggler-bar navbar-kebab"></span>
                    </button>
                    <div class="collapse navbar-collapse justify-content-end" id="navigation">
                        <form>

                        </form>
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link" href="#pablo">
                                    
                                    <p>
                                        <span class="d-lg-none d-md-block">Stats</span>
                                    </p>
                                </a>
                            </li>
                           
                                
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="user.py">""")
profilefunc.cookie()
print("""<i class="now-ui-icons users_single-02"></i>
                                    <p>
                                        <span class="d-lg-none d-md-block">Account</span>
                                    </p>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        <div class="panel-header panel-header-sm">
            </div>
            <div class="content">
                <div class="row">
                    <div class="col-md-8">
                        <div class="card">
                            <div class="card-header">
                                <h3 class="title">User Profile</h3>
                            </div>
                            <div class="card-body">
                                <form>
                                    <div class="row">
                                        <div class="col-md-5 pr-1">
                                            <div class="form-group">
                                        <div class="col-md-12 pr-1">
                                            <div class="form-group">
                                                <label>Full Name</label>
                                                <input type="text" class="form-control" style="color:red;" placeholder='""")
profilefunc.fullname()
print("""'value="">
                                            </div>
                                        </div>
                                            </div>
                                        </div>
                                        
                                        <div class="col-md-3 px-1">
                                            <div class="form-group">
                                                <label>Username</label>
                                                <input type="text" class="form-control" style="color:black;"  placeholder='""")
profilefunc.username()
print("""'value="">
                                            </div>
                                        </div>
                                        <div class="col-md-4 pl-1">
                                            <div class="form-group">
                                                <label for="exampleInputEmail1">Email address</label>
                                                <input type="email" class="form-control";"  placeholder='""")
profilefunc.email()
print("""'value="">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        
                                       <!-- <div class="col-md-6 pl-1">
                                            <div class="form-group">
                                                <label>Last Name</label>
                                                <input type="text" class="form-control" placeholder="Last Name" value="">
                                            </div>
                                        </div> -->
                                    </div>
                                
                                    <div class="row">
                                        <!-- <div class="col-md-12">
                                            <div class="form-group">
                                                <label>Address</label>
                                                <input type="text" class="form-control" placeholder="Home Address" value="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09">
                                            </div>
                                        </div> -->
                                        <!-- <div class="col-md-6 pr-1">
                                            <div class="form-group">
                                                <label>Mobile Number</label>
                                                <input type="text" class="form-control" placeholder="123456789" value="">
                                            </div>
                                        </div> -->
                                        <div class="col-md-6 pr-1">
                                            <div class="form-group">
                                                <label>Password</label>
                                                <input type="password" class="form-control" placeholder="******" disabled value="">
                                            </div>
                                        </div>
                                    </div>""")
profilefunc.signoutt()

print("""<div class="row">

                                    </div>
                                    <div class="row">
                                       
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card card-user">
                            <div class="image">
                            
                            </div>
                            <div class="card-body">
                                <div class="author">
                                    <a href="#">
                                        <img class="avatar border-gray" src="http://localhost/docs/img/userloads/""")
profilefunc.image()
print(""" "alt="..."><br>""")
print("""<h5 class="title">""")
profilefunc.uname()
print("""<br><br>""")
print("""<form method = "post" enctype = "multipart/form-data" action = "savefile.py">
<input type="file" name="file"><br>
<br><div class="col-xs-12">
<div class="view-all">
<input type="submit" name="submit" value="upload">
					</div>
					</form>
</div>""")
print("""</h5>Welcome to Helpzone, give your career a great push and achieve your dreams.<br>
                Explore the best from Helpzone. 
                                    </a>
                                    
                                </div>
                                
                            </div>
                            <hr>
                            <div class="button-container">
                                <button href="#" class="btn btn-neutral btn-icon btn-round btn-lg">
                                    <i class="fab fa-facebook-f"></i>
                                </button>
                                <button href="#" class="btn btn-neutral btn-icon btn-round btn-lg">
                                    <i class="fab fa-twitter"></i>
                                </button>
                                <button href="#" class="btn btn-neutral btn-icon btn-round btn-lg">
                                    <i class="fab fa-google-plus-g"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <footer class="footer">
                <div class="container-fluid">
                    <nav>
                       
                    </nav>
                    <div class="copyright">
                        &copy;
                        <script>
                            document.write(new Date().getFullYear())
                        </script>, Designed by
                        <a href="https://www.invisionapp.com" target="_blank">and</a>. Coded by
                        <a href="https://www.creative-tim.com" target="_blank">Anmol Bansal</a>.
                    </div>
                </div>
            </footer>
        </div>
    </div>
</body>
<!--   Core JS Files   -->
<script src="../../docs/profile/assets/js/core/jquery.min.js"></script>
<script src="../../docs/profile/assets/js/core/popper.min.js"></script>
<script src="../../docs/profile/assets/js/core/bootstrap.min.js"></script>
<script src="../../docs/profile/assets/js/plugins/perfect-scrollbar.jquery.min.js"></script>
<!--  Google Maps Plugin    -->
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>
<!-- Chart JS -->
<script src="../../docs/profile/assets/js/plugins/chartjs.min.js"></script>
<!--  Notifications Plugin    -->
<script src="../../docs/profile/assets/js/plugins/bootstrap-notify.js"></script>
<!-- Control Center for Now Ui Dashboard: parallax effects, scripts for the example pages etc -->
<script src="../../docs/profile/assets/js/now-ui-dashboard.js?v=1.0.1"></script>
<!-- Now Ui Dashboard DEMO methods, don't include it in your project! -->
<script src="../../docs/profile/assets/demo/demo.js"></script>

</html>""")
