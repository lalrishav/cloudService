#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print data
action = data.getvalue("action")
dname = data.getvalue("acton").split(".")[0]
user = data.getvalue("user")
print "<pre>"

print "<a href='/fe/extendsize.php?dname={}'>Click here</a>".format(dname)


print "</pre>"