import os
if 'HTTP_COOKIE' in os.environ: #can access all cookies from client
    cookie_string = os.environ.get ( 'HTTP_COOKIE' )
    e1 = cookies.SimpleCookie()
    e1.load(cookie_string)
    redirect = e1['shop'].value
    print("Content-type: text/html\n")
    print("<script> window.location.assign('index1.py'); </script>")

db = sqlite3.connect("guidance.db")
c = db.cursor()

e = cookies.SimpleCookie()
form = cgi.FieldStorage()
email = form.getvalue('email')
username = form.getvalue('uname')
fullname = form.getvalue('name')
pwd = form.getvalue('password')
flag=0
cursor=c.execute('SELECT username from cgitable where username=?',(username,) )
rows = cursor.fetchall()

def uname():
    for row in rows:
        if (username in row):
            print("<font color='#ed4956'>&nbsp;",username,"has been taken. Please try another.</font> ")
        global flag
        flag=1

kursor = c.execute ('SELECT email from cgitable where email=?',(email,) )
rrows=kursor.fetchall()

def mail():
    for row in rrows:
        if(email in row):
            print("<font color='#ed4956'>&nbsp;",+str(email)+"has been taken. Please try another.</font>")
        global flag
        flag=2

def create():
    if(flag == 0):
        if(username==None):
            print("Please enter a username")
        else:
            c.execute('insert into cgitable(username,fullname,email,pwd) values(?,?,?,?)',(username,fullname,email,pwd) )
            print("<script> window.location.assign('signin.py'); </script>")
            db.commit()
            db.close()
            
            
