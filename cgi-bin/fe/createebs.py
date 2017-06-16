#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print "<pre>"
print data
zone = data.getvalue("zone")
size = data.getvalue("size")
user = data.getvalue("user")

print "aws ec2 create-volume --size {} --region us-west-2 --availability-zone {} --volume-type gp2".format(size,zone)

vdetail = commands.getoutput("sudo aws ec2 create-volume --size {} --region us-west-2 --availability-zone {} --volume-type gp2".format(size,zone))
print vdetail
vid = (vdetail.split(", ")[3]).split(":")[1]
if(os.path.exists("/database/{}".format(user))==False):
	commands.getoutput("sudo mkdir  /database/{}".format(user))
	commands.getoutput("sudo chmod 777 /database/{}".format(user))
if(os.path.exists("/database/{}/volumes".format(user))==False):
	commands.getoutput("sudo mkdir /database/{}/volumes".format(user))
	commands.getoutput("sudo chmod 777 /database/{}/volumes".format(user))
vid=vid[2:-1]
print ("({})".format(vid))
f=open("/database/{}/volumes/{}".format(user,vid),'a')
f.close()
print "done"





print "</pre>"