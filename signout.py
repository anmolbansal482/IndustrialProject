#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
import cgi
import sqlite3
import os
import Cookie
e = Cookie.SimpleCookie ( )
e['shop'] = None  # assign a value
e['pass'] = None
#e['firstt']= first
#e['emaill']= emaill
e['shop']['expires'] = 0 * 0 * 0
e['pass']['expires'] = 0 * 0 * 0
print(e)
print ("Content-type:text/html\r\n\r\n")
print "<script>  window.location.assign('signin.py');  </script>"