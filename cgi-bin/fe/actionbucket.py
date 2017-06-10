#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
print data

bucket = data.getvalue("acton")
user = data.getvalue("user")

print "<pre>"

print commands.getstatusoutput("sudo aws s3 rb s3://{} --force".format(bucket))
print commands.getstatusoutput("sudo rm -rf /database/{}/s3/{}".format(user,bucket))
print "successfully deleted"
print "</pre>"