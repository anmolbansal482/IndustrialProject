#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling

# start signin function #
import cgi
import sqlite3
import os
import cgitb; cgitb.enable()
import Cookie

db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )
def sign():
    if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            #username = e1['shop'].value
            print  "<script>  window.location.assign('index1.py');   </script>"

# create the cookie
e = Cookie.SimpleCookie ( )
form = cgi.FieldStorage ( ) #get input from html form
passs = form.getvalue ( 'pwd' )
name = form.getvalue ( 'username' )
flag = 0 # flag to check stage
cursor = c.execute ( 'SELECT * from cgitable where username=? and password=?', (name, passs,) )#to check username and password in database

for row in cursor: #to print feilds from database
    dun = row[2]
    #name = row[0]
    #emaill = row [1]
    dps = row[3]
    if (dun == name and dps == passs):
        e['shop'] = name  # assign a value
        e['pass'] = passs
        #e['firstt']= first
        #e['lastt'] = last
        #e['emaill']= emaill
        e['shop']['expires'] = 24 * 60 * 60
        e['pass']['expires'] = 24 * 60 * 60  # set the xpires time
        #e['firstt']['expires'] = 24 * 60 * 60
        #e['lastt']['expires'] = 24 * 60 * 60
        #e['emaill']['expires'] = 24 * 60 * 60

        print ( e )  # print the header, starting with the cookie
        print("Content-type:text/html\r\n\r\n")
        print "<script>  window.location.assign('index1.py');  </script>"  #redirect to homepage if it is login

        flag = 1
def flago():
    if (flag == 0):
        if (name == None or passs == None):

            print ( "" )
        else:

            print "<p style='style='color:#fff;'</p>Wrong Username or Password"
db.commit ( )
db.close ( )

# end signin function #