#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print "<pre>"
print data
sid = data.getvalue("acton")
action = data.getvalue("action")
user = data.getvalue("user")

def terminate(sid,action):
	print commands.getoutput("sudo aws ec2 delete-snapshot --snapshot-id {}".format(sid))
	print commands.getoutput("sudo rm -rf /database/{}/snapshots/{}".format(user,sid))
	print "successfully deleted"

def createVolume(sid,action):
	print "<meta http-equiv='refresh' content='2;url=/fe/revertsnap.php?sid={}'/>".format(sid)
	#print commands.getoutput("sudo aws ec2 create-volume --region us-west-2  --snapshot-id {} --volume-type gp2")
	#print "success"
	

if(action=="terminate"):
	terminate(sid,action)
elif(action=="createVolume"):
	createVolume(sid,action)