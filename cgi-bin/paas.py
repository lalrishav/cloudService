#!/usr/bin/python2

import cgi,commands,os,time


print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
service = data.getvalue("platform")
user = data.getvalue("uname")
print "<pre>"
x=commands.getoutput("sudo docker run -itd lalrishav")
print x

print commands.getoutput("sudo docker exec {} usermod -s /usr/bin/{} shell".format(x,service))
commands.getoutput("sudo docker exec {} service shellinaboxd start".format(x))
ip = commands.getoutput("sudo docker exec {} hostname -i".format(x))
print ip
print commands.getstatusoutput("sudo mkdir /database/{}".format(user))
print commands.getstatusoutput("sudo mkdir /database/{}/paas".format(user))
print commands.getstatusoutput("sudo chmod 777 /database/{}/paas".format(user))
import random
curr_time = random.randrange(1,100000)
f=open("/database/{}/paas/{}.{}".format(user,service,curr_time),'a')
f.write(x)
f.close()

print ip

print "<a href='http://{}:4200'>Click here to open</a>".format(ip)

print "</pre>"
