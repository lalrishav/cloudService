#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print "<pre>"
print data
vid = data.getvalue("vid")
amiId = data.getvalue("amiId")
user = data.getvalue("user")
command = "aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(vid,amiId)
attach = commands.getstatusoutput("sudo "+command)
print attach
if(attach[0]==0):
	f=open("/database/{}/volumes/{}".format(user,vid),'a')
	f.write(amiId)
	f.close()
	print "done"






















print "</pre>"