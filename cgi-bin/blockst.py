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
print "-----------------------------------------------------------------------------------------"
print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

msg = "<target iqn.2003-11.{}.com:adhoc>\nbacking-store  /dev/mapper/myhd-{}\n</target>".format(dname,dname)
print "<pre>"
print msg
print "<pre>"

f = open("/etc/tgt/tgtd.conf",'a')
f.write("\n"+msg)
f.close()
commands.getoutput("systemctl restart tgtd")
print "11111111111111111111"
f = open("/var/www/html/{}.sh".format(dname),'w')
data = "#!/usr/bin/python2\nimport os\nos.system('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.238 --discover')\nos.system('iscsiadm --mode node --targetname iqn.2003-11.{}.com:adhoc --portal 192.168.122.238:3260 --login')".format(dname)
f.write(data)
f.close()
print "<a href='/{}.sh'>Click here to download</a>".format(dname)


