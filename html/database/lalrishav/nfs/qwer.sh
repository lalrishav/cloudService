#!/usr/bin/python2
import os
os.system('systemctl restart rpcbind')
os.system('mkdir /media/qwer')
os.system('mount -t nfs 192.168.1.200:/mnt/qwer /media/qwer')
