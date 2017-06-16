#!/usr/bin/python2

import cgi,commands,os,time


print "Content-type:text/html"
print ""

x=commands.getoutput("sudo docker run -itd alexl/broadway")
ip = commands.getoutput("sudo docker exec {} hostname -i".format(x))
print "<a href='http://{}:8080'>CLick here to connect</a>".format(ip)