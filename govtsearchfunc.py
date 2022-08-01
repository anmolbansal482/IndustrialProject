#!C:\python27\python.exe
# -*- coding: utf-8 -*-
# import modules for cgi handling

import cgi
import sqlite3
import os
import cgitb;

cgitb.enable()
import Cookie

db = sqlite3.connect("guidance.db")
c = db.cursor()
# NEW except for the call to processInput
form = cgi.FieldStorage()  # standard cgi script lines to here!
# use format of next two lines with YOUR names and default data
id = form.getfirst("search")  # process input into a page


def cookie():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
        cookie_string = os.environ.get('HTTP_COOKIE')
        e1 = Cookie.SimpleCookie()
        e1.load(cookie_string)
        username = e1['shop'].value
        user = username[:4] + '..!'
        print "<a id='dropdown-link2' data-target='user.py' href='user.py'role='button' >Hi@", user, "</a>"
    else:
        print "Hello Guest !"


def signoutt():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
        cookie_string = os.environ.get('HTTP_COOKIE')
        e1 = Cookie.SimpleCookie()
        e1.load(cookie_string)
        username = e1['shop'].value
        print "<a id='dropdown-link2' data-target='signout.py' href='signout.py'role='button' >Sign Out!</a>"
    else:
        print "<a id='dropdown-link2' data-target='signin.py' href='signin.py'role='button' >Sign In!</a>"


# end index1.py functions #


def title():
    c.execute('SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        title = row[1]
        print(title)


def description():
    c.execute(' SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        desc = row[5]
        print(desc)


def req():
    c.execute(' SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        req = row[3]
        print(req)


def scope():
    c.execute(' SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        sco = row[4]
        print(sco)


def field():
    c.execute(' SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        feeld = row[2]
        print(feeld)


def tabs():
    c.execute(' SELECT * from govtsearch where id=? ', (id,))
    rows = c.fetchall()
    for row in rows:
        title = row[1]
        feeld = row[2]
        req = row[3]
        scope = row[4]
        desc = row[5]


        print("""<section class="page-title" data-parallax="scroll" data-image-src="../../docs/img/other/tricolour_indian_flag_hd_5k-3840x2400.jpg">
		<div class="container">
                        <div class="row">
                        <div class="col-xs-12">

        <h1>""")
        print(title)
        print("""</h1>

				</div>
			</div>
		</div>
	    </section>""")

        print("""<div class="col-xs-12 col-sm-12 col-md-12 col-lg-12 offset-1">
					<div class="article__text">
						<h1>""")

        # starts printing the field
        print(feeld)

        print("""</h1>""")

        # ends printing the field

        # starts printing description

        print("""<p>""")
        print(desc)
        print("""<p>""")
        # end printing description

        print("""<h1>Requirements and Syllabus : </h1>""")

        print(req)
        print("""</p>""")

        print("""<h1>Scope : </h1>""")
        print("""<p>""")
        print(scope)
        print("""</p>""")

        print("""</div>""")
    # print("""<img src="../../docs/img/other/1_ADaIoXSLtb3oDe64ENeVtg.jpeg" alt="">



