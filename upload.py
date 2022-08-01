#!C:\python27\python.exe
#import modules for cgi handling

import cgi
import os
import sqlite3
import cgitb; cgitb.enable()
import Cookie


if 'HTTP_COOKIE' in os.environ:  # can access all cookies sent from the client using the HTTP_COOKIE
        #  environment variable.
            cookie_string = os.environ.get ( 'HTTP_COOKIE' )
            e1 = Cookie.SimpleCookie ( )
            e1.load ( cookie_string )
            username = e1['shop'].value
            
form = cgi.FieldStorage()
db = sqlite3.connect("guidance.db")
c = db.cursor()
db.row_factory = sqlite3.Row #file will be fetched through this line
print("Content-type:text/html\n")
cursor = c.execute('SELECT * from cgitable where username=?',())

def images():
    for row in cursor:
        m = row['image']
        print('<img src="../../../userloads/' + m + '" height = "100%" width = "100%">')
        print("Uploaded Successfully")
        print("<script>  window.location.assign('user.py');   </script>")


db.commit()
db.close()
          

