#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print "<pre>"
print data
aid = data.getvalue("acton")
action = data.getvalue("action")
user = data.getvalue("user")

def terminate(aid,action):
	print commands.getoutput("sudo aws ec2 deregister-image --image-id {}".format(aid))
	print commands.getoutput("sudo rm -rf /database/{}/ami/{}".format(user,aid))
	print "successfully deleted"

def createInstance(aid,action):
	#print "<meta http-equiv='refresh' content='2;url=/fe/revertsnap.php?aid={}'/>".format(aid)
	instId = commands.getstatusoutput("sudo aws ec2 run-instances --image-id {} --security-group-ids sg-41be9a3a --count 1 --instance-type t2.micro --key-name adhocvirt --query 'Instances[0].InstanceId'".format(aid))
	print instId[1]
	if instId[0]==0:
		f=open("/database/{}/instance/{}".format(user,instId[1][1:-1]),'a')
		f.close()
		print "done"

	

if(action=="terminate"):
	terminate(aid,action)
elif(action=="createInstance"):
	createInstance(aid,action)