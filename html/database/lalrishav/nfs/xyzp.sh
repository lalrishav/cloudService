#!/usr/bin/python2
import os
os.system('systemctl restart rpcbind')
os.system('mkdir /media/xyzp')
os.system('mount -t nfs 192.168.1.200:/var/www/html/users/lalrishav/xyzp /media/xyzp')
