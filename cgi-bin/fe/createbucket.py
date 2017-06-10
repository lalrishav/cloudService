#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
print data
user = data.getvalue("user")
name = data.getvalue("name")

print "<pre>"
if os.path.exists("/database/{}/s3".format(user))==False:
	print commands.getstatusoutput("sudo mkdir /database/{}/s3".format(user))
	print commands.getstatusoutput("sudo chmod 777 /database/{}/s3".format(user))

mb = commands.getstatusoutput("sudo aws s3 mb s3://{}".format(name))
print mb
if(mb[0]==0):
	f=open("/database/{}/s3/{}".format(user,name),'a')
	f.close()
	print "done"
else:
	print "<h2>Bucket name not available.Try another name</h2>"
	print "<meta http-equiv='refresh' content='2;url=/fe/createbucket.php'>"

print "</pre>"