#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
os1 = data.getvalue("os")
ram = data.getvalue("ram")
cpu = data.getvalue("cpu")
print "<pre>"
print os.system("sudo virt-install --name {} --ram {} --vcpu {} --cdrom /root/Desktop/lal.iso  --nodisk --graphics vnc,listen=0.0.0.0,port=5916 &".format(os1,ram,cpu))

#print os.system("sudo virt-install --name qw --ram 1 --vcpu 1 --cdrom /root/Desktop/lal.iso  --nodisk --graphics vnc,listen=0.0.0.0,port=5915 &")
print os.system("sudo date")
print os.system("sudo mkdir /hellob")
print os.system("sudo websockify --web=/usr/share/novnc 6080 0.0.0.0:5916 &")
print os.system("sudo mkdir /root/Desktop/oye1")





print "</pre>"
