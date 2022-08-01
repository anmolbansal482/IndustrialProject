#!C:\python27\python.exe
# -*- coding: utf-8 -*-
#import modules for cgi handling
# start signup.py #

import cgi
import sqlite3
import smtplib
import cgitb; cgitb.enable()
import random

a='abcdefghijklmnopqrstuvwxyz1234567890'
password = ''
for i in range(34):
    password = password+random.choice(a)

form = cgi.FieldStorage()
emailc= form.getfirst('emailchange')

db = sqlite3.connect ( "guidance.db" )
c = db.cursor ( )

def smail():
    c.execute('SELECT * from cgitable where email = ?',(emailc,))
    rows = c.fetchall()
    for row in rows:
        if (emailc == None):
            print("<font color:#fff>&nbps; Please enter your email")
        global ema
        ema = row[1]
        c.execute('update cgitable set reset=? where email=? ',(password, ema,))
        db.commit()
        db.close()

    to = emailc
    subject = "Reset your password"
    text = "http://localhost/cgi-bin/anmolpython/change.py?email="+str(emailc)+"&key="+str(password)+""

    gmail_sender = "bansalanmol786@gmail.com"
    gmail_passwd = "jaggabrand482"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    name = ('HelpZone<bansalanmol786@gmail.com>')
    server.ehlo()
    server.login(gmail_sender, gmail_passwd)

    body = '\r\n'.join([
        'To: %s' % to,
        'From: %s' % name,
        'Subject: %s' % subject,
        '',
        text
    ])
    try:
        server.sendmail(name, [to], body)
        print("<font color:#fff>&nbsp; Email sent. Please Check your mail</p>")
    except:
        print("")
    server.quit()
