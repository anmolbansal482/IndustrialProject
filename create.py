#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
import cgi
print ("Content-type:text/html\r\n\r\n")
import sqlite3
db=sqlite3.connect('guidance.db')
print("Database created")
db.close()
