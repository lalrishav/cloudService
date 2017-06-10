#!/usr/bin/python2

#code to run terminat and create image of a instnace


import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print data
user = data.getvalue("user")
action = data.getvalue("action")
imageId = data.getvalue("acton")
print "<pre>"

pageTerminate = '''
<center><h3><span style="color:blue">Your instance has been successfully terminated<br><a href='/fe/viewinstance.php'>View Instnaces</a></span></h3></center>
'''

pageCreateImage = '''
<center><h3><span style="color:blue">Your image has been successfully created<br><a href='/fe/ami.php'>View Images</a></span></h3></center>
'''




def terminate(imageId):
	status = commands.getstatusoutput("sudo aws ec2 terminate-instances --instance-ids {}".format(imageId,))
	#print status
	if status[0]==0:
		commands.getoutput("rm -rf /database/{}/instance/{}".format(user,imageId))
		print pageTerminate


def createImage(imageId):
	instId = commands.getstatusoutput("sudo aws ec2 create-image --instance-id {} --name 'server of {}' --no-reboot".format(imageId,imageId))
	print instId[1]
	instId = instId[1]
	instId = instId.split(":")[1].rpartition("}")
	instId=instId[0][1:-1][1:-1]
	print instId
	if os.path.exists("/database/{}/ami".format(user))==False:
		commands.getoutput("sudo mkdir /database/{}/ami".format(user))
		commands.getoutput("sudo chmod 777 /database/{}/ami".format(user))
	f=open("/database/{}/ami/{}".format(user,instId),'a')
	f.write(imageId)
	f.close()
	print "done"


if action=="terminate":
	terminate(imageId)
elif action=="createImage":
	createImage(imageId)




print "</pre>"