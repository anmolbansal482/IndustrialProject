#!C:\python27\python.exe -u
# -*- coding: utf-8 -*-


import cgi
import os
import sqlite3
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
fileitem = form['file']
import Cookie
def sign():
    if 'HTTP_COOKIE' in os.environ:
        cookie_string = os.environ.get('HTTP_COOKIE')
        e1 = Cookie.SimpleCookie()
        e1.load (cookie_string)
        global username
        global fileitem
        username = e1['shop'].value

    else:
        print "<script> window,location.assign('index1.py'); </script>"


def img():
    if fileitem.filename:
        #strip leading path from file name
        user = username
        fn = os.path.basename(fileitem.filename)
        open('../../htdocs/docs/img/userloads/' +fn, 'wb').write(fileitem.file.read())
        print('Profile Picture "'+fn+'" Uploaded Successfully')
        print("<script> window.location.assign('user.py'); </script>")
        db = sqlite3.connect("guidance.db")
        c = db.cursor()
        c.execute('update cgitable set image=? where username=?',(fn, user))

        print("")
        db.commit()
        db.close()
    else:
        print("<script> window.location.assign('user.py'); </script>")
        print("Please Choose a File")

print("Content-Type: text/html\n")
print("""<html><body><p>""")
sign()
img()
print("""</p></body></html>""")


    
