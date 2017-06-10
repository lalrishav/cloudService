#!/usr/bin/python2

import cgi,commands,os,time


print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
service = data.getvalue("service")
print "<pre>"
x=commands.getoutput("sudo docker run -itd lalrishav")
print x

print commands.getoutput("sudo docker exec {} usermod -s /usr/bin/{} shell".format(x,service))
commands.getoutput("sudo docker exec {} service shellinaboxd start".format(x))
ip = commands.getoutput("sudo docker exec {} hostname -i".format(x))

print ip

print "<a href='http://{}:4200'>Clicke here to open</a>".format(ip)

print "</pre>"
