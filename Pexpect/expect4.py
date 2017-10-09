#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: xxx.run.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-28 15:04:54
#  Description: 命令行自动输入密码执行ssh命令
#########################################################################

# /usr/bin/python

import pexpect
import sys

pexpect.run('ssh lcs@192.168.1.12 ls -l /home/lcs', events={
    'yes':'yes',
    'password:': '123456\n'
}, logfile=sys.stdout)
