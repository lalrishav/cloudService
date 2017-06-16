#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
print "<pre>"
data = cgi.FieldStorage()
print data

dname = data.getvalue("dname")
uname = data.getvalue("uname")

print commands.getoutput("sudo lvextend --size +200M /dev/mapper/myhd-{}".format(dname))
print commands.getoutput("sudo resize2fs /dev/mapper/myhd-{}".format(dname))
print "Successfully extended the size"
print"</pre>