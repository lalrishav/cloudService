#!/usr/bin/python2
import os
os.system('service restart rpcbind')
os.system('mkdir /media/aa')
os.system('mount -t nfs 127.0.0.1:/mnt/aa /media/aa')