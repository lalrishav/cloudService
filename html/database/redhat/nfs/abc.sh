#!/usr/bin/python2
import os
os.system('iptables -F;setenforce 0')
os.system('systemctl restart rpcbind')
os.system('mkdir /media/abc')
os.system('mount -t nfs 192.168.1.200:/var/www/html/users/redhat/abc /media/abc')
