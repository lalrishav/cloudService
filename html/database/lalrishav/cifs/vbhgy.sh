#!/usr/bin/python2
import os
os.system('systemctl restart smb')
os.system('mkdir /media/vbhgy'
os.system('mount -t cifs -o username=vbhgy //192.168.1.200/vbhgy /media/vbhgy'
