#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: expect1.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-28 10:15:58
#########################################################################

#/usr/bin/python
import pexpect
import sys
child = pexpect.spawn('ssh lcs@192.168.1.13')
child.expect("password:")
child.sendline("123456")
child.expect('\$')
child.sendline('ls -l /home/lcs')
child.logfile = sys.stdout
child.expect('\$')
