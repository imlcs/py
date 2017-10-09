#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: xxx.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-28 10:57:06
#########################################################################

# /usr/bin/python
import pexpect
import sys


def commands():
    child.sendline('123456')
    child.expect('\$')
    child.sendline('ip addr | grep inet')
    #child.logfile = sys.stdout
    child.expect('\$')
    child.interact()


def ssh(hostinfo):
    global child
    child = pexpect.spawn('ssh {}'.format(hostinfo))
    index = child.expect(['yes', 'password' ,pexpect.TIMEOUT])
    if index == 0:
        child.sendline('yes')
        commands()
    elif index == 1:
        commands()
    else:
        print('TIMEOUT')


if __name__ == '__main__':
    hostinfo = raw_input('Pls input ssh host, expmale(user@host -p port):')
    ssh(hostinfo)
