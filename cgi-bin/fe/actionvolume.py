#!/usr/bin/python2
import cgi,os,commands,time
print "Content-type:text/html"
print ""
data = cgi.FieldStorage()
print "<pre>"
print data
vid = data.getvalue("acton")
action = data.getvalue("action")
user = data.getvalue("user")
def terminate(vid,action):
	print commands.getoutput("sudo aws ec2 delete-volume --volume-id {}".format(vid))
	print commands.getoutput("sudo rm -rf /database/{}/volumes/{}".format(user,vid))
	print "successfully deleted"

def createSnapshot(vid,action):
	sdetail = commands.getstatusoutput("sudo aws ec2 create-snapshot --volume-id {} --description 'This is my root {} snapshot.'".format(vid,vid))
	if sdetail[0]==0:
		snapshotId = ((sdetail[1].split(", ")[7]).split(": ")[1])[1:-1]
		print "({})".format(snapshotId);
		if(os.path.exists("/database/{}/snapshots".format(user))==False):
			commands.getoutput("sudo mkdir /database/{}/snapshots".format(user))
			commands.getoutput("sudo chmod 777 /database/{}/snapshots".format(user))
		f=open("/database/{}/snapshots/{}".format(user,snapshotId),'a')
		f.write(vid)
		f.close()
		print "successfully created"
if(action=="terminate"):
	terminate(vid,action)
elif(action=="createSnapshot"):
	createSnapshot(vid,action)