#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

user = data.getvalue("user")
name = data.getvalue("acton")
action = data.getvalue("action")

def terminate(name):
	print ""

def editInstance(name):
	print "Redirecting......"
	print "<meta http-equiv='refresh' content='1; URL=/fe/editinstance.php?name={}'>".format(name)




if action=="terminate":
	terminate(name)
if action=="edit":
	editInstance(name)