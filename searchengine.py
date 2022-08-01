#!C:\python27\python.exe
# -*- coding: utf-8 -*-
import cgi
import sqlite3
import os
import cgitb; cgitb.enable()
import Cookie
db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )
form = cgi.FieldStorage ( ) #get input from html form
srch = form.getvalue ( 'search' )
e = Cookie.SimpleCookie ( )
def cookie():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            user = username[:4] + '..!'
            print ( "<a class='chat-button' href=''>Hi@"+str(user))
    else:
            print ( "<a class='chat-button' href='http://localhost/cgi-bin/anmolpython/signup.py'>Hello Guest !" )


def signoutt():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            print "<a class='signin-button' href='logout.py'>Sign Out</a>"
    else:
            print "<a class='ignin-button' href='signin.py'>Sign in</a>"

def article(): #function to call article
    c.execute ( 'SELECT * from articlesearch where title or field like ?', ('%'+srch+'%',))

    rows = c.fetchall ( )
    for row in rows:
        fild = row[6]
        desc =  row[2]
        id = row[0]
        decc = (desc[:250] + '...')


        print("""<div class='col-xs-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="articlesresult.py>""")

        print("""<div class='col-xs-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="articlesresult.py>""")


        print("</a></div>")
        print("""<div class="article-text">""")

        print("""<div class="card article-card">
									<div class="card-wrap">
										<a href='articlesresult.py?search=""")
        print(id)
        print("""'</a>
										
										<img src="../../docs/img/other/106645.jpg" alt="">
									
										<div class="category category--pink"></div>
										
										<h3>""")

        print(fild)
        print("""</h3>
										<p>""")
        print(decc)
        print("""</p>
										<!-- Statistic 
										<ul class="statistic">
											<li class="likes">
												<a href="articlesresult.py"><i class="zmdi zmdi-favorite-outline"></i></a>
												<span>231</span>
											</li>
											<li class="comments">
												<a href="articlesresult.py comments-article-id1"><i class="zmdi zmdi-comment-outline"></i></a>
												<span>421</span>
											</li>
										</ul>
										 End Statistic -->
									                </div>
								                </div>
								            </div>
								        </div>
								    </div>
								</div>""")


def univ():  # function to call article
    c.execute('SELECT * from topu where title  like ?', ('%' + srch + '%',))
    rows = c.fetchall()
    for row in rows:
        fildd = row[1]
        idd = row[0]

        print("""<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="university.py>""")

        print("""<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="university.py>""")

        print("</a></div>")
        print("""<div class="article-text">""")

        print("""<div class="card article-card">
									<div class="card-wrap">
										<a href='university.py?topu=""")
        print(idd)
        print("""'</a>

										<img src="../../docs/img/other/106645.jpg" alt="">

										<div class="category category--pink"></div>

										<h3>""")

        print(fildd)
        print("""</h3>
										<p>""")
        print("""</p>
        										
        									                </div>
        								                </div>
        								            </div>
        								        </div>
        								    </div>
        								</div>""")


def gov():  # function to call article
    c.execute('SELECT * from govtsearch where desc like ?', ('%' + srch + '%',))
    rows = c.fetchall()
    for row in rows:
        fildd = row[2]
        idd = row[0]
        desc = row[5]
        decc = (desc[:250] + '...')
        print("""<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="govtsearch.py?search=>""")

        print("""<div class='col-xs-12 col-sm-12 col-md-12 col-lg-12'>
                <div class="article-summary">
                    <div class="article-img"><img src="" alt="" /></div><div class="article-title"><a href="govtsearch.py?search=>""")

        print("</a></div>")
        print("""<div class="article-text">""")

        print("""<div class="card article-card">
									<div class="card-wrap">
										<a href='govtsearch.py?search=""")
        print(idd)
        print("""'</a>

										<img src="../../docs/img/other/106645.jpg" alt="">

										<div class="category category--pink"></div>

										<h3>""")

        print(fildd)
        print("""</h3>
										<p>""")

        print(decc)
        print("""</p>
        									                </div>
        								                </div>
        								            </div>
        								        </div>
        								    </div>
        								</div>""")

        print("""</p>

        									                </div>
        								                </div>
        								            </div>
        								        </div>
        								    </div>
        								</div>""")







