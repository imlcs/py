#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: xxx.run.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-28 15:04:54
#########################################################################

# /usr/bin/python

import pexpect
import sys

res = pexpect.run('lftp lcs@192.168.1.12', events={
    'Password:': '123456\n',
    '>':'put expect4.py\nexit\n',
    })
print(res)
#}, logfile=sys.stdout)
