#!/usr/bin/python2

import cgi,commands

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dname = data.getvalue("dname")
dsize = data.getvalue("dsize")

print dname


x = commands.getstatusoutput("sudo lvcreate --name" + " " + dname + " " + "--size" + " " + dsize +    " " + "myhd")
print "<pre>"
print x
print "</pre>"
print "<pre>"
print commands.getoutput("sudo mkfs.ext4 /dev/mapper/myhd-" + dname )
print "</pre>"
print "<pre>"
print commands.getoutput("sudo mkdir /mnt/" + dname)
print "</pre>"
print "<pre>"
print commands.getoutput("sudo mount /dev/mapper/myhd-" + dname + " " + "/mnt/" + dname)
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
msg = "\n" + "/mnt/" + dname + "       " + "*(rw,no_root_squash)"
print msg
f.write(msg)
f.close()


f = open("/var/www/html/staa.sh",'w')
wr = "#!/usr/bin/python2\nimport os\nos.system('service restart rpcbind')\nos.system('mkdir /media/" + dname + "')\nos.system('mount -t nfs 127.0.0.1:/mnt/" + dname + " /media/" + dname + "')"
print "<pre>"
print wr
print "</pre>"
f.write(wr)
f.close()
print commands.getoutput("systemctl restart nfs-server")
print commands.getoutput("systemctl restart rpcbind")
print "yooooooo!!!!"
print "<a href='/staa.sh'> download </a>"

