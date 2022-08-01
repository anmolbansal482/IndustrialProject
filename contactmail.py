#!C:\python27\python.exe
# -*- coding: utf-8 -*-
import smtplib
import cgi

form = cgi.FieldStorage()
email = form.getvalue('email')
firstname = form.getvalue('fname')
lastname = form.getvalue('lname')
num = form.getvalue('mob')
message = form.getvalue('mess')


to = "bansalanmol786@gmail.com"
subject = firstname + lastname +  " ,Feedback Form"
text = "email : " + email + " Mobile : " + num + " Message : "  + message

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
    print("Content-type:text/html\r\n\r\n")
    print("<script>window.location.assign('contact.py');</script>")
except:
    print("")
    server.quit()
