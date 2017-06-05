#!/usr/bin/python2

import cgi,commands,os
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""


data = cgi.FieldStorage()

uname = data.getvalue("user")
password = "redhat"

msg = "#!/bin/bash\nsystemctl start vsftpd\nsystemctl start httpd\nsystemctl start nfs-server\nsystemctl rpcbind\nmount /dev/mapper/myhd-webserver /var/www/html\nexportfs -r\nsetenforce 0\niptables -F\nuseradd {}\necho q | passwd {} --stdin\nmount -t nfs 127.0.0.1:/var/www/html /home/{}/".format(uname,uname,uname)

f=open("/record/{}.txt".format(uname),'w')
f.write(msg)
f.close()

print "hello"

print commands.getoutput("sudo aws ec2 run-instances --image-id ami-52606f2b --security-group-ids sg-41be9a3a --count 1 --user-data file:///record/{}.txt   --instance-type t2.micro --key-name adhocvirt  --query 'Instances[0].InstanceId'".format(uname))

print "hellooosss"
