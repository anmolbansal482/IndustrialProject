#!C:\python27\python.exe
# -*- coding: utf-8 -*-

import cgi
import sqlite3
import smtplib
import random
import cgitb; cgitb.enable()

a='abcdefghijklmnopqrstuvwxyz1234567890'
password = ''
for i in range(34):
    password = password+random.choice(a)

form = cgi.FieldStorage()

emm = form.getfirst('email')
urlkey = form.getfirst('key')

emid = form.getvalue('eid')
hidkey = form.getvalue('hkey')

newp = form.getvalue('nwp')
conp = form.getvalue('cop')
db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )

flag = 0
def user():
    global flag
    flag = 1
    c.execute('SELECT * from cgitable where email=?', (emm,))


def resetone():
    c.execute('SELECT * from cgitable where email=?',(emm,))
    rows = c.fetchall()
    for row in rows:
        dkey = row[9]
        if (urlkey == dkey):
            print("""<section class="m-b-lg">
            <form action="change.py">
                <div class="list-group">
                    <div class="list-group-item">
                        <input type="text" name="nwp" required placeholder="New Password" class="form-control no-border">
                    </div>
                 <div class="list-group-item">
                        <input type="text" name="cop" required placeholder="Confirm Password" class="form-control no-border">
                     </div>
                         <input type="hidden" name="eid" value="""+str(emm)+""">
                         <input type="hidden" name="hkey" value="""+str(urlkey)+""">
                 </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">Change</button>
            </form>
            </section>""")
        else:
            print("<h1 style='text-align:center; color:#fff;'> Url not found</h1>")




def resettwo():
    c.execute('SELECT * from cgitable where email=?',(emid,))
    rows = c.fetchall()
    for row in rows:
        datakey = row[9]
        if (datakey == hidkey):
            if (newp == None):
                print("Please enter a password")
            elif (newp == conp):
                c.execute('update cgitable set password=? where email=?',(newp,emid,))
                c.execute('update cgitable set reset=? where email=?', (password, emid,))
                db.commit()
                db.close()
                print("<h1 style='text-align:center; color:#fff;'> Password Updated</h1>")
            elif (newp != conp):
                print("<h1 style='text-align:center; color:#fff;'> Password did not match</h1>")
        else:
            print("<h1 style='text-align:center; color:#fff;'>Oops! Invalid Url</h1>")








