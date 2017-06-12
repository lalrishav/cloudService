#!/usr/bin/python2
import os
os.system('systemctl restart smb')
os.system('mkdir /media/werbhg'
os.system('mount -t cifs -o username=werbhg //192.168.1.200/werbhg /media/werbhg'
