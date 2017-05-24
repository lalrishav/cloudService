#!/usr/bin/python2
import cgi
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
x = data.getvalue("val")

send = "#!/usr/bin/python2\nimport os"+"\n" +"os.system('ssh -X root@192.168.10.100 " + x + "')"
f = open("/var/www/html/" + x + ".sh",'w')
f.write(send)
f.close()
st = "<meta http-equiv='refresh' content='0;url=/" + x + ".sh'>"
print st
