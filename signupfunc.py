#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
# start signup.py #

import cgi
import os
import sqlite3
import smtplib
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
            username = e1['shop'].value

            print "<script>  window.location.assign('index1.py');  </script>"
db = sqlite3.connect("guidance.db")
c = db.cursor()

#e = cookies.SimpleCookie()
form = cgi.FieldStorage()
email = form.getvalue('email')
username = form.getvalue('username')
fullname = form.getvalue('name')
pwd = form.getvalue('pass')
password = form.getvalue('repeat-pass')
num = form.getvalue('mobile')

flag = 0
cursor = c.execute('SELECT * from cgitable where username=?',(username,))
rows = cursor.fetchall()
def uname():
    for row in rows:
        if (username in row):
            print "<font color='#ed4956'>&nbsp;", (username),"isn't available. Please try another.</font>"

        global flag
        flag = 1
        break
kursor = c.execute('SELECT email from cgitable where email=?',(email,))
rrows = kursor.fetchall()
def mail():
    for row in rrows:
        if(email in row):
            print "<font color='#ed4956'>&nbsp; ",(email),"is associated with another account.</font>"

        global flag
        flag = 2
        break

    to = email
    subject = "Confirmation"
    text = "Thanks for registering with Helpzone. Explore the most for your career."

    gmail_sender = "bansalanmol786@gmail.com"
    gmail_passwd = "jaggabrand482"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_sender, gmail_passwd)

    body = '\r\n'.join([
        'To: %s' % to,
        'From: %s' % gmail_sender,
        'Subject: %s' % subject,
        '',
        text
    ])
    try:
        server.sendmail(gmail_sender, [to], body)
        print('')
    except:
        print("")
    server.quit()

#def confirm():
    #for row in rrows:
        #if(password != pwd):
            #print("<font color='#ed4956'>&nbsp; ",(password),"password did not match.")
        #global flag
        #flag = 4
        #break
def confirmpass():
    if (password == pwd):
        global pwdd
        pwdd = pwd
    else:
        pwdd = 0
        print("<font color='#ed4956'>&nbsp; Please write same password in both")
        global flag
        flag = 2


def create():
    if(flag == 0):
        if(username == None or pwdd == 0):
            print("")
        else:
            c.execute('insert into cgitable(name,username,email, password,mobile)values (?,?,?,?,?)',(fullname,username,email,pwdd,num))

            print "<script>  window.location.assign('signin.py'); </script>"
            db.commit()
            db.close()




# end signup.py function #