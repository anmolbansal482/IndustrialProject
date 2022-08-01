#!C:\python27\python.exe
# -*- coding: utf-8 -*-
import cgi
import sqlite3
import os
from http import cookies
db=sqlite3.connect('guidance.db')
c=db.cursor()
e=cookies.SimpleCookie()
form=cgi.FieldStorage()
password=form.getvalue('pwd')
uname=form.getvalue('username')
flag=0

cursor=c.execute('SELECT * from cgitable where username=? and password=? ',(uname,password))
for row in cursor:
    dun=row[2]
    dps=row[3]
    if(dun==uname and dps==password):
        e['shop']=uname
        e['pass']=password
        e['pass']['expires']=30*60
        e['shop']['expires']=30*60
        print(e)
        print('Content-type:text/html\n')
        print("<script> window.location.assign('index1.py'); </script>")
        flag=1
print('Content-type:text/html\n')
if(flag==0):
    if(uname==None or password==None):
        print("Please enter field")
    else:
        print("Wrong username or password")
db.commit()
db.close()
