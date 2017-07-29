#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: sanjiao.py
#  Author: lcs
#  Mail: 15224800531@163.com 
#  Created Time: 2017-07-28 19:33:44
#########################################################################

#/usr/bin/python
import os
dev = []
ip = []
ipinfo = os.popen('ip addr | grep "inet" | awk -F"[ /]+" \'{print $3,$NF}\'')
for info in ipinfo.readlines():
    #print(info),
    info = info.split(' ')
    ip.append(info[0])
    dev.append(info[1].split('\n')[0])

new_dict = dict(zip(dev,ip))
print(new_dict)
