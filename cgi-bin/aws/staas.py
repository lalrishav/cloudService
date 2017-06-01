#!/usr/bin/python2
import cgi,commands
server_ip = "0.0.0.0"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dname = data.getvalue("dname")
dsize = data.getvalue("dsize")
uname = data.getvalue("uname")
print dname
print dsize
print uname

instance_id = "i-05327d8531056e3e9"
instance_type = "t2.micro"
availability_zone = "us-west-2c"

#print "sudo aws ec2 create-volume --size {} --region us-east-2 --availability-zone {} --volume-type gp2".format(dsize,availability_zone)+"\n"
x=commands.getoutput("sudo aws ec2 create-volume --size {} --region us-west-2 --availability-zone us-west-2c --volume-type gp2".format(dsize))
vid = (x.split(","))[3].split(":")[1]
print "<pre>"
print commands.getoutput("sudo aws ec2 attach-volume --volume-id {} --instance-id {} --region us-west-2 --device /dev/sdf".format(vid,instance_id))

print "</pre>"


















print dname
