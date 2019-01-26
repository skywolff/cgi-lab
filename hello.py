#!/usr/bin/env python3
import cgi
import cgitb
import os
import json
import urllib
cgitb.enable()

# environ = {key:value for k,value in os.environ.items()}
environ = dict(os.environ)
print("Content-type: text/html")
print()
print("<!doctype html>")
print("<head>")
print("<title>HELLO</title>")
print("</head>")
print("<H1>The Hello Page</H1>")
print()

# report user browser
print("<H2>User Agent:</H2>")
print(environ["HTTP_USER_AGENT"])

# report values of the query parameters
print("<H2>Query String:</H2>")
print(urllib.parse.parse_qs(environ["QUERY_STRING"]))

# serve environment in JSON
print("<H2>Environ:</H2>")
print("<pre>")
print(json.dumps(environ, indent=4))
print("</pre>")

