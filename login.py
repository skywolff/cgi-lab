#!/usr/bin/env python3
import cgi
import cgitb
import os
import templates
import secret
cgitb.enable()

# check cookie for login
username = password = None
cookies = os.environ.get("HTTP_COOKIE")
cookies = cookies.split(';')
for cookie in cookies:
    cookie = cookie.strip()
    if 'username' in cookie:
        username = cookie.split('=')[1]
    elif "password" in cookie:
        password = cookie.split('=')[1]

if username and password:
    print(templates.secret_page(username, password))

elif os.environ.get("REQUEST_METHOD", "GET") == "POST":   # no cookies was set
    form = cgi.FieldStorage()

    if "username" not in form or "password" not in form:
        print("<H2>Error</H2>")
        print("Please fill in the  name and addr fields.")
    else:
        username = form["username"].value
        password = form["password"].value
        print("<p>")
        print("username:", form["username"].value)
        print("password:", form["password"].value)
        print("</p>")

        if username == secret.username and password == secret.password:
            # correct login, set cookie
            print("Set-Cookie: username={};".format(username))
            print("Set-Cookie: password={};".format(password))
            print(templates.secret_page(username, password))
        else:
            print(templates.after_login_incorrect())
else:
    print(templates.login_page(), end="\n\n")