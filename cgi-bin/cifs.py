#!/usr/bin/python2

import cgi,commands,time
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dname = data.getvalue("dname")
dsize = data.getvalue("dsize")

print dname

print commands.getoutput("sudo setenforce 0")
print commands.getoutput("sudo iptables -F")

x = commands.getoutput("sudo lvcreate --name" + " " + dname + " " + "--size" + " " + dsize +    " " + "myhd")
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

send = "[{}]\npath=/mnt/{}\nwritable=yes".format(dname,dname)
print "<pre>"
print send
print "</pre>"
print "-----------------------------"
print commands.getoutput("sudo systemctl restart smb")

# commands.getoutput("sudo lvremove /dev/mapper/myhd-{}".format(dname))
print commands.getstatusoutput("sudo useradd {}".format(dname))
print "<pre>"
time.sleep(10)
print commands.getoutput("(echo {}; echo {})|sudo smbpasswd -a -s {}".format(dname,dname,dname))
print "</pre>"

f = open("/etc/samba/smb.conf",'a')
f.write("\n"+send)
f.close()

print "--------------------------"

print commands.getoutput("sudo systemctl restart smb")
print dname
print commands.getoutput("sudo chown "+dname +" /mnt/"+dname)
print "1111111111111111111111111111111111111111111111111111"

f = open("/var/www/html/cifs.sh",'w')
print "--------------------wsefrgfsefdgtfhefrt--------------"
msg = "#!/usr/bin/python2\nimport os\nos.system('systemctl restart smb')\nos.system('mkdir /media/{}'.format(dname))\nos.system('mount -t cifs -o username={} //192.168.1.200/{} /media/{}'.format(dname,dname,dname)\n".format(dname,dname,dname,dname)
print "abcdabcdbabcdbdbdbdbdbdbdbd"
print "<pre>"
print msg
print "</pre>"
f.write(msg)
f.close()
print "fgryhdusakdkfghjgfkdsdfjhugrsejidoklcv bvjgfuiriejdc"
print "<a href='/cifs.sh'>download here</a>"



