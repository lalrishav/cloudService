#!/usr/bin/python2

import cgi,commands,os,subprocess
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
os1 = data.getvalue("os")
ram = data.getvalue("ram")
cpu = data.getvalue("cpu")
user = data.getvalue('user')
print "<pre>"

print os.system("qrencode -s 16*16 -o /var/www/html/qr/wow.png http://192.168.1.100:6080")

print os.system("sudo virt-install --name {} --ram {} --vcpu {} --cdrom /root/Desktop/lal.iso  --nodisk --graphics vnc,listen=0.0.0.0,port=5918 &".format(os1,ram,cpu))

#print os.system("sudo virt-install --name qw --ram 1 --vcpu 1 --cdrom /root/Desktop/lal.iso  --nodisk --graphics vnc,listen=0.0.0.0,port=5915 &")
print os.system("sudo websockify --web=/usr/share/novnc 6080 0.0.0.0:5918 &")

print "<h2>Method 1</h2>"
print "<h3><a href='http://192.168.1.100:6080'>Click here to view your Os</a></h3><br><br>"
print "<h2>Method 2</h2>"
print "<img src='/qr/wow.png' width=250 height=250></img>"
print "<h3>Scan above qrcode to view your Os</h3>"
print "\n\n"
print "<h3><a href='/qr/wow.png' download>Click here</a> to save the qrcode for future use</h3>".format(user)





print "</pre>"
