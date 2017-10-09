#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: port.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-13 21:56:18
#########################################################################

#/usr/bin/python

import sys,threading
from socket import *

host = "127.0.0.1" if len(sys.argv)==1 else sys.argv[1]
portList = [i for i in range(1,65535)]
scanList = []
lock = threading.Lock()
print('Please waiting... From ',host)


def scanPort(port):
    try:
        tcp = socket(AF_INET,SOCK_STREAM)
        tcp.connect((host,port))
    except:
        pass
    else:
        if lock.acquire():
            print('[+]port',port,'open')
            lock.release()
    finally:
        tcp.close()

for p in portList:
    t = threading.Thread(target=scanPort,args=(p,))
    scanList.append(t)
for i in range(len(portList)):
    scanList[i].start()
for i in range(len(portList)):
    scanList[i].join()
