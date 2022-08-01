#!C:\python27\python.exe
# -*- coding: utf-8 -*-
# import modules from cgi
import cgi
import os
import sqlite3
import cgitb; cgitb.enable()
import Cookie

db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )

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

def eng(): #function to call article
    engg = ('Engineering')
    c.execute ( 'SELECT * from topu where category = ?',(engg,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")


def laww(): #function to call article
    laaw = ('Law')
    c.execute ( 'SELECT * from topu where category = ?',(laaw,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")


def bua(): #function to call article
    buaa = ('Business Administration')
    c.execute ( 'SELECT * from topu where category = ?',(buaa,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")


def medi(): #function to call article
    med = ('Medical')
    c.execute ( 'SELECT * from topu where category = ?',(med,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")


def hotel(): #function to call article
    hm = ('Hotel Management')
    c.execute ( 'SELECT * from topu where category = ?',(hm,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")


def fashion(): #function to call article
    ft = ('Fashion Technology')
    c.execute ( 'SELECT * from topu where category = ?',(ft,) )
    rows = c.fetchall ( )
    for row in rows:
        title = row[1]
        idd = row[0]
        print("""<li><a href='university.py?topu=""")
        print(idd)
        print("""'>""")
        print(title)
        print("""</a></li>""")




