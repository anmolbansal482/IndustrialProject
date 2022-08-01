#!C:\Python27\python.exe
# -*- coding: utf-8 -*-

print ( "Content-type:text/html\r\n\r\n" )
print ( """<!doctype html>""" )

print ( """<html lang="en" """ )
print("""<head>
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
</head>""")

print ( """

        <form class="navbar-form navbar-left input-s-lg m-t m-l-n-xs hidden-xs" method='get' action='http://localhost/cgi-bin/anmolpython/search.py'>
        <div class="form-group">
          <div class="input-group">
            <span class="input-group-btn">
              <button type="submit" class="btn btn-sm bg-white b-white btn-icon"><i class="fa fa-search"></i></button>
            </span>
            <input type="text" name="search" class="form-control input-sm no-border" style="width :600% ;"placeholder="Search ">            
          </div>
        </div>
      </form>
      <ul class="nav navbar-nav navbar-right m-n hidden-xs nav-user user">
        <li class="hidden-xs">


          <section class="dropdown-menu aside-xl animated flipInY">
            <section class="panel bg-white">
              <div class="panel-heading b-light bg-light">
                <strong>You have <span class="count">2</span> notifications</strong>
              </div>
              <div class="list-group list-group-alt">
                <a href="#" class="media list-group-item">
                  <span class="pull-left thumb-sm">
                    <img src='""" )

print ( """' alt="..." class="img-circle">
                  </span>
                  <span class="media-body block m-b-none">
                    Use awesome animate.css<br>
                    <small class="text-muted">10 minutes ago</small>
                  </span>
                </a>
                <a href="#" class="media list-group-item">
                  <span class="media-body block m-b-none">
                    1.0 initial released<br>
                    <small class="text-muted">1 hour ago</small>
                  </span>
                </a>
              </div>

            </section>
          </section>
        </li>
        <li class="dropdown">
          <a href="profile.py" class="dropdown-toggle" data-toggle="dropdown">
            <span class="thumb-sm avatar pull-left">""" )

print ( """</span>""" )

#profunction.username ( )
print ( """</a>

        </li>
      </ul>      
    </header>
    <section>
      <section class="hbox stretch">
        <!-- .aside -->

        <!-- /.aside -->
        <section id="content">
          <section class="vbox">
            <section class="scrollable padder">
              <div class="m-b-md">

              </div>


              <section class="panel panel-default">""")

print("""<div class="panel-body">   <!-- form begin -->
                  <form enctype="multipart/form-data" class="form-horizontal" method="post" action="../../cgi-bin/anmolpython/writedata.py">
                    <div class="form-group">


                    </div>
                    <div class="line line-dashed b-b line-lg pull-in"></div>
                    <div class="form-group">
                      <label class="col-sm-2 control-label">Name of University</label>
                      <div class="col-sm-10">
                        <input type="text"  name="title" class="form-control">

                      </div>
                    </div>
                    <div class="form-group">


                    </div>

					<div class="form-group">
                      <label class="col-sm-8 control-label">category</label>
                      <div class="col-sm-12">
						<textarea name="cat" class="form-control" rows="50" cols="50"></textarea>

                      </div>
                    </div>

					<!-- <div class="form-group">
                      <label class="col-sm-2 control-label">Requirement</label>
                      <div class="col-sm-10">
						<textarea name="req" class="form-control" rows="12" cols="50"></textarea>

                      </div>
                    </div> -->


					<!-- <div class="form-group">
                      <label class="col-sm-2 control-label"> Scope</label>
                      <div class="col-sm-10">
						<textarea name="sco" class="form-control" rows="12" cols="50"></textarea>

                      </div>
                    </div> -->

					<!-- <div class="form-group">
                      <label class="col-sm-2 control-label">Top-uni</label>
                      <div class="col-sm-10">
						<textarea name="to" class="form-control" rows="12" cols="50"></textarea>

                      </div>
                    </div> -->
                    
                    
					<!-- <div class="form-group">
                      <label class="col-sm-2 control-label">Field</label>
                      <div class="col-sm-10">
						<textarea name="fiel" class="form-control" rows="12" cols="50"></textarea>

                      </div>
                    </div> -->


                      <label class="col-sm-2 control-label">logo</label>

                        <input type="file"  name="file">
                    <div class="form-group">
                      <div class="col-sm-4 col-sm-offset-2">

                        
                      <!-- <label class="col-sm-2 control-label">back</label>

                        <input type="file"  name="file2">
                    <div class="form-group">
                      <div class="col-sm-4 col-sm-offset-2"> -->


                        <button type="submit" class="btn btn-primary">Submit</button>
                      </div>
                    </div>
                  </form> <!-- form end -->
                </div>
              </section>
            </section>
          </section>
          <a href="#" class="hide nav-off-screen-block" data-toggle="class:nav-off-screen" data-target="#nav"></a>
        </section>
      </section>
    </section>
  </section>
  <script src="http://localhost/medical/files/profile/js/jquery.min.js"></script>
  <!-- Bootstrap -->
  <script src="http://localhost/medical/files/profile/js/bootstrap.js"></script>
  <!-- App -->
  <script src="http://localhost/medical/files/profile/js/app.js"></script>  
  <script src="http://localhost/medical/files/profile/js/slimscroll/jquery.slimscroll.min.js"></script>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
  </div>""" )

print ( """</body></html>""" )
