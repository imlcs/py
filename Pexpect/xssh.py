#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: xssh.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-30 15:22:58
#  Description: 
#########################################################################

#/usr/bin/python

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()
    host = raw_input('Hostname:')
    user = raw_input('Username:')
    passwd = getpass.getpass('Password:')

    s.login(host,user,passwd)
    s.sendline('uptime')
    s.prompt()
    print(s.before)
    s.sendline('ls -l')
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh, e:
    print('pxssh failed on login.')
    print(str(e))