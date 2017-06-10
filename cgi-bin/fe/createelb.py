#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
name = data.getvalue("name")
user = data.getvalue("user")
length = len(data)
count = 0 
#print data
key = []

for i in data:
	if(count >=length-2):
		continue
		count = count + 1
	print i
	key.append(i)
	count = count + 1
print "<pre>"
#print commands.getstatusoutput("sudo aws elb register-instances-with-load-balancer --load-balancer-name {} --instances {}".format(name,key))
if os.path.exists("/database/{}/elb")==False:
	print commands.getstatusoutput("sudo mkdir /database/{}/elb".format(user))
	print commands.getstatusoutput("sudo chmod 777 /database/{}/elb".format(user))
dns = commands.getstatusoutput("sudo aws elb create-load-balancer --load-balancer-name {} --listeners 'Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80' --availability-zones us-west-2a us-west-2b us-west-2c".format(name))

print dns

print commands.getstatusoutput("sudo mkdir /database/{}/elb/{}".format(user,name))
print commands.getstatusoutput("sudo chmod 777 /database/{}/elb/{}".format(user,name))

dn = dns[1][18:-3]
print dn
f=open("/database/{}/elb/{}/{}.dns".format(user,name,dn),'a')
f.close()

for j in key:
	print "----------------"
	print commands.getstatusoutput("sudo aws elb register-instances-with-load-balancer --load-balancer-name {} --instances {}".format(name,j))
	f=open("/database/{}/elb/{}/{}".format(user,name,j),'a')
	f.close()

print "</pre>"




