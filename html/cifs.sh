#!/usr/bin/python2
import os
os.system('systemctl restart smb')
os.system('mkdir /mnt/manku'.format(dname))
os.system('mount -t cifs -o username=manku //192.168.1.200/manku /media/manku'.format(dname,dname,dname)
