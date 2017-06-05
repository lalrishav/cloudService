#!/usr/bin/python2

import cgi,commands,os
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dname = data.getvalue("dname")
dsize = data.getvalue("dsize")
uname = data.getvalue("uname")


#vgname = "myhd"



print dname
print "-------------------"
print commands.getoutput("sudo setenforce 0")
print commands.getoutput("sudo iptables -F")

x = commands.getstatusoutput("sudo lvcreate --name" + " " + dname + " " + "--size" + " " + dsize +    " " + "myhd")
print "<pre>"
print x
print "</pre>"
print "<pre>"
print commands.getoutput("sudo mkfs.ext4 /dev/mapper/myhd-" + dname )
print "</pre>"
print "<pre>"
print "@@@@@@@@@@@"
if(os.path.exists(uname)==False):
	commands.getoutput("sudo mkdir /var/www/html/users/" + uname)
       #commands.getoutput("sudo chmod 777 /var/www/html/users/"+uname)
mnt_point = "/var/www/html/users/" + uname + "/" + dname
print commands.getoutput("sudo mkdir "+mnt_point)
#print commands.getoutput("sudo chmod 777 "+mnt_point)
print "</pre>"
print "<pre>"
print commands.getoutput("sudo mount /dev/mapper/myhd-" + dname + " " + mnt_point)
print "</pre>"
print "-----------------------------------------------------------------------------------------"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

print commands.getoutput("sudo systemctl restart rpcbind")
print commands.getoutput("sudo systemctl restart nfs-server")
print commands.getoutput("sudo iptables -F")
print commands.getoutput("sudo setenforce 0")
print "hello"
print ""
print "----------------------------------------------------------------------------------------------"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

f = open("/etc/exports",'a')
print ""
msg = "\n" + mnt_point + "       " + "*(rw,no_root_squash)"
print msg
f.write(msg)
f.close()


'''f = open("/var/www/html/staa.sh",'w')

wr = "#!/usr/bin/python2\nimport os\nos.system('service restart rpcbind')\nos.system('mkdir /media/" + dname + "')\nos.system('mount -t nfs " +  server_ip + ":/mnt/" + dname + " /media/" + dname + "')\n"
print "<pre>"
print wr
print "</pre>"
f.write(wr)
f.close()'''
print commands.getoutput("sudo systemctl restart nfs-server")
print commands.getoutput("sudo systemctl restart rpcbind")
print commands.getoutput("sudo exportfs -r")
print commands.getoutput("sudo setenforce 0")
print commands.getoutput("sudo iptables -F")
#print commands.getoutput("sudo apachectl graceful")
print "Your drive has been created Successfully"
#commands.getoutput("sudo systemctl stop httpd")
#commands.getoutput("sudo systemctl start httpd")
print "<a href='/users/{}/{}'>See your drive</a>".format(uname,dname)


