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
if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
        cookie_string = os.environ.get('HTTP_COOKIE')
        e1 = Cookie.SimpleCookie()
        e1.load(cookie_string)
        username = e1['shop'].value
else:
      print("Content-type: text/html\n\n")
      print ("<script> window.location.assign('signin.py'); </script>")


form = cgi.FieldStorage()
op = form.getvalue('oldpass')
np = form.getvalue('newpass')
cp = form.getvalue('confirmpass')

#password = form.getvalue('repeat-pass')
flag = 0
cursor = c.execute('SELECT * from cgitable where username=?',(username,))
rows = cursor.fetchall()
for row in rows:
    old = row[3]
    flag = 1

def oldp():
    if op == None:
        up = op
    elif old == op:
        global flag
        flag = 2
    else:
        print("Wrong Password")

def cpass():
    if (flag == 2):
        if(np == cp):
          c.execute('update cgitable set password = ? where username = ?', (np, username),)
          print("Password changed")

          db.commit()
          db.close()
          print("Content-type: text/html\n\n")
          print ("<script> window.location.assign('signin.py'); </script>")
        else:
          print("Re-enter")
