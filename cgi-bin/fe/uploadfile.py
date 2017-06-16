#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
print data
path = data.getvalue("path")
bucket = data.getvalue("bucket")
print "<pre>"
print commands.getoutput("sudo aws s3 cp {} s3://{}/".format(path,bucket))
print "</pre>"