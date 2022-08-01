#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling

# start profilefunc function #
import cgi
import sqlite3
import os
import cgitb; cgitb.enable()
db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )
form = cgi.FieldStorage()
loca = form.getvalue ( 'location' )
import Cookie

def locate():
    cookie_string = os.environ.get('HTTP_COOKIE')
    e = Cookie.SimpleCookie()
    e.load(cookie_string)
    uname = e['shop'].value

    db = sqlite3.connect("guidance.db")
    c = db.cursor()
    c.execute('update cgitable set Location=? where username=?', (loca,uname))
    db.commit()
    db.close()

def ulocate():
    cookie_string = os.environ.get('HTTP_COOKIE')
    e = Cookie.SimpleCookie()
    e.load(cookie_string)
    usname = e['shop'].value
    cursor1 = c.execute('SELECT * from cgitable where username=?',(usname,))
    rows = cursor1.fetchall()
    for row in rows:
        mlocation = row[8]
        print(mlocation)

def cookie():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            #firstname = e1['firstt'].value
            #lastname = e1['lastt'].value
            print ( "<a class='chat-button' href=''>Hi@"+str(username))
    else:
            print ( "<a class='chat-button' href='http://localhost/cgi-bin/anmolpython/signup.py'>Hello Guest !" )


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

#function to call username with cookie

def username():
    if 'HTTP_COOKIE' in os.environ:
        cookie_string = os.environ.get('HTTP_COOKIE')
        e1 = Cookie.SimpleCookie()
        e1.load( cookie_string)
        username = e1['shop'].value
        print("@"+str(username))


# to print username of profile #
def uname():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            print "Hi@",username
    else:
            print "Hello Guest !"
# to print username of profile

def fullname():
    cookie_string = os.environ.get("HTTP_cookie")
    e = Cookie.SimpleCookie()
    e.load(cookie_string)
    uname = e['shop'].value
    c.execute('SELECT * from cgitable where username=?',(uname,) )
    rows = c.fetchall()
    for row in rows:
        fname = row[0]
        print(fname)


def email():
    cookie_string = os.environ.get('HTTP_COOKIE')
    e = Cookie.SimpleCookie()
    e.load(cookie_string)
    uname = e['shop'].value
    c.execute('SELECT * from cgitable where username=?',(uname,))
    rows = c.fetchall()
    for row in rows:
        email = row[1]
        print(email)



def image():
    cookie_string = os.environ.get('HTTP_COOKIE')
    e = Cookie.SimpleCookie()
    e.load(cookie_string)
    uname = e['shop'].value
    c.execute('SELECT * from cgitable where username=?',(uname,))
    rows = c.fetchall()
    for row in rows:
        img = row[7]
        print(img)





# start article functions #

#def title():
    #cookie_string = os.environ.get('HTTP_COOKIE')
    #e = cookies.SimpleCookie()
    #e.load(cookie_string)
    #uname = e['shop'].value

    #c.execute ('SELECT * from articletable where author=?',(uname))
    #rows = c.fetchall()
    #for row in rows:
        #title = row[1]
        #print("Title",title)

#def desc():
    #cookie_string = os.environ.get('HTTP_COOKIE')
    #e = cookies.SimpleCookie()
    #e.load(cookie_string)
    #uname = e['shop'].value

    #c.execute('SELECT * from articletable where author=?',(uname))
    #rows = c.fetchall()
    #for row in rows:
        #desc = row[2]
        #print("Description",desc)
