#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: modify_buff_size.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-04 16:41:23
#########################################################################

#/usr/bin/python
import socket

SEND_BUFF_SIZE = 4096
RECV_BUFF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size before: %d" % buffsize)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.TCP_NODELAY, 1)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            SEND_BUFF_SIZE)
    sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_SNDBUF,
            RECV_BUFF_SIZE)
    buffsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size now: %d" % buffsize)

if __name__ == '__main__':
    modify_buff_size()
