#!/usr/bin/python2
import os
os.system('systemctl restart smb')
os.system('mkdir /media/yu')
os.system('mount -t cifs -o username=yu //192.168.1.200/yu /media/yu')
