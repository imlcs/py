#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: sanjiao.py
#  Author: lcs
#  Mail: 15224800531@163.com 
#  Created Time: 2017-07-28 17:22:13
#########################################################################

#/usr/bin/python
import time
import os

#now_time = time.strftime('%F_%T')
now_time = time.strftime('%F')
disk_status = ''.join(os.popen('df -h').readlines())

f = file('/tmp/' + now_time + '.log','w')
f.write('%s' % disk_status)
f.flush()
f.close()
