#!/usr/bin/python2

import os,commands
a =['firefox','gedit','vncv','virt-','gnome-terminal']
while True:
	for i in a:
		x=commands.getstatusoutput("ps -e | grep "+i)
		u = ""
		if x[0]!=0:
			continue
		else:
			t=x[1].split('?')[0]
			os.system("kill "+t)
		
