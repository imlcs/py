#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: socket_timeout.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-08-24 22:51:24
#########################################################################

#/usr/bin/python
import socket

def get_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Default socket timeout: %s' % s.gettimeout())
    s.settimeout(100)
    print('Current socket timeout: %s' % s.gettimeout())

if __name__ == '__main__':
    get_socket_timeout()

