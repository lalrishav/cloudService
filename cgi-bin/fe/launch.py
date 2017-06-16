#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print data
ino = data.getvalue("ino")
user = data.getvalue("user")
imageId = data.getvalue("imageId")
secId = data.getvalue("securityGroup")
print "<pre>"
print "hello"
for i in range (0,int(ino)):
	print "sudo aws ec2 run-instances --image-id {} --count 1 --instance-type t2.micro --key-name adhocvirt --security-group-ids {}".format(imageId,secId)
	instId=commands.getoutput("sudo aws ec2 run-instances --image-id {} --count 1 --instance-type t2.micro --key-name adhocvirt --security-group-ids {} --query 'Instances[0].InstanceId'".format(imageId,secId))
	print instId
	if(os.path.exists("/database/{}".format(user))==False):
		commands.getoutput("sudo mkdir  /database/{}".format(user))
		commands.getoutput("sudo mkdir /database/{}/instance".format(user))
		commands.getoutput("sudo chmod 777 /database/{}".format(user))
		commands.getoutput("sudo chmod 777 /database/{}/instance".format(user))
	commands.getoutput("sudo mkdir /database/{}/instance".format(user))
	commands.getoutput("sudo chmod 777 /database/{}".format(user))
	commands.getoutput("sudo chmod 777 /database/{}/instance".format(user))
	f=open("/database/{}/instance/{}".format(user,instId[1:-1]),'a')
	f.close()



print "</pre>"
