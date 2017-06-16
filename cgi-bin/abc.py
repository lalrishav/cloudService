#!/usr/bin/python2
import cgi,commands
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
x = data.getvalue("service")
uname = data.getvalue("uname")

send = "#!/usr/bin/python2\nimport os"+"\n" +"os.system('ssh -X 192.168.1.200 " + x + "')"

commands.getoutput("sudo mkdir /var/www/html/database/{}".format(uname))
commands.getoutput("sudo chmod 777 /var/www/html/database/{}".format(uname))

commands.getoutput("sudo mkdir /var/www/html/database/{}/saas".format(uname))
commands.getoutput("sudo chmod 777 /var/www/html/database/{}/saas".format(uname))

f = open("/var/www/html/database/{}/saas/{}.sh".format(uname,x),'w')
f.write(send)
f.close()
st = "<meta http-equiv='refresh' content='0;url=/database/{}/saas/{}.sh'>".format(uname,x)
print st
