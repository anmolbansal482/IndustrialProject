#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
import cgi
import sqlite3
print ("Content-type:text/html\r\n\r\n")
db=sqlite3.connect("guidance.db")
print('Database updated')
c=db.cursor()
c.execute('alter table topu add column category ;')
db.commit()
db.close()
