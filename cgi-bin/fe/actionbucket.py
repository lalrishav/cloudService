#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
print data

bucket = data.getvalue("acton")
user = data.getvalue("user")
action = data.getvalue("action")

print "<pre>"
if action=="terminate":
	print commands.getstatusoutput("sudo aws s3 rb s3://{} --force".format(bucket))
	print commands.getstatusoutput("sudo rm -rf /database/{}/s3/{}".format(user,bucket))
	print "successfully deleted"
elif action=="uploadfile":
	print "<a href='/uploadfile.php?b={}'>Click here</a>".format(bucket)
elif action=="uploaddir":
	print "<a href='/uploaddir.php?b={}'>Click here</a>".format(bucket)
print "</pre>"