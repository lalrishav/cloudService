#!/usr/bin/python2
import os
os.system('service restart rpcbind')
os.system('mkdir /media/laalu')
os.system('mount -t nfs 192.168.1.200:/mnt/laalu /media/laalu')
