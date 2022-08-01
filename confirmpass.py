def confirm():
    for row in rrows:
        if(password != pwd):
            print("<font color='#ed4956'>&nbsp; password did not match.")
        global flag
        flag = 3
        break
