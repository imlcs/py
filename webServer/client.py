#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: client.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-27 10:36:08
#########################################################################

#/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',80))

sock.send(b'test')
data = sock.recv(1024)
print(data.decode())
