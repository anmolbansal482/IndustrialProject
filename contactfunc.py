#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling

import cgi
import os
import smtplib
import sqlite3
import cgitb; cgitb.enable()
import Cookie
db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )
def cookie():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            user = username[:4] + '..!'
            print "<a id='dropdown-link2' data-target='user.py' href='user.py'role='button' >Hi@",user,"</a>"
    else:
            print  "Hello Guest !"

def signoutt():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            print ( "<a id='dropdown-link2' data-target='signout.py' href='signout.py'role='button' >Sign Out!</a>" )
    else:
            print ( "<a id='dropdown-link2' data-target='signin.py' href='signin.py'role='button' >Sign In!</a>" )

# end index1.py functions #



