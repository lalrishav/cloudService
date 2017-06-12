#!/usr/bin/python2

import cgi,commands,time
server_ip = "192.168.1.200"

print "Content-type:text/html"
print ""
print "<head>"
print "<style>#abc{background-color:green;height:100px;width:1200px;padding:5px;overflow:auto;color:black}</style>"
print "</head>"
print "<center><h3>LOG</h3></center>"
print "<center><div id='abc'>"
print "<note>"
data = cgi.FieldStorage()

dname = data.getvalue("dname")
dsize = data.getvalue("dsize")
uname = data.getvalue("uname")


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
mnt_point = "/var/www/html/users/" + uname + "/" + dname

print commands.getoutput("sudo mkdir "+mnt_point)
print "</pre>"

print "<pre>"
print commands.getoutput("sudo mount /dev/mapper/myhd-" + dname + " " + mnt_point)
print "</pre>"
print "-----------------------------------------------------------------------------------------"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

send = "[{}]\npath={}\nwritable=yes".format(dname,mnt_point)
print "<pre>"
print send
print "</pre>"
print "-----------------------------"
print "<pre>"
print commands.getoutput("sudo systemctl restart smb")

# commands.getoutput("sudo lvremove /dev/mapper/myhd-{}".format(dname))
print commands.getstatusoutput("sudo useradd {}".format(dname))
print "</pre>"
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
print commands.getoutput("sudo chown "+dname +" " + mnt_point)
print "1111111111111111111111111111111111111111111111111111"
save_point = "/var/www/html/database/{}".format(uname)
commands.getoutput("mkdir " + save_point)
commands.getoutput("mkdir " + save_point + "/cifs")
commands.getoutput("chmod 777 " + save_point)
commands.getoutput("chmod 777 "+save_point+"/cifs")



f = open("/var/www/html/database/{}/cifs/{}.sh".format(uname,dname),'w')
print "--------------------wsefrgfsefdgtfhefrt--------------"
msg = "#!/usr/bin/python2\nimport os\nos.system('systemctl restart smb')\nos.system('mkdir /media/{}'\nos.system('mount -t cifs -o username={} //192.168.1.200/{} /media/{}'\n".format(dname,dname,dname,dname)
print "abcdabcdbabcdbdbdbdbdbdbdbd"
print "<pre>"
print msg
print "</pre>"
f.write(msg)
f.close()
print "fgryhdusakdkfghjgfkdsdfjhugrsejidoklcv bvjgfuiriejdc"
print "<a href='/cifs.sh'>download here</a>"
print "</div>"



