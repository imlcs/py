#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: pexpect_ssh.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-27 16:22:19
#########################################################################

#/usr/bin/python

import pexpect
import getpass,os,sys

def ssh_command(user,host,password,command):
    ssh_newkey = 'yes'
    global child
    child = pexpect.spawn('ssh  %s@%s %s' % (user,host,command))
    child.logfile = sys.stdout
    i = child.expect([pexpect.TIMEOUT, ssh_newkey,'password:'])

    if i == 0:
        print(child.before)
        print(child.after)
        return None

    if i == 1:
        child.sendline('yes')
        child.expect('password:')
        i = child.expect([pexpect.TIMEOUT, 'password:'])

        if i == 0:
            print(child.before)
            print(child.after)
            return None
        child.sendline(password)
        return  child
    else:
        child.sendline(password)
        return  child

def main():
    host = raw_input('Hostname: ')
    user = raw_input('Username: ')
    password = getpass.getpass()
    command = raw_input('Enter the command: ')

    chlid = ssh_command(user,host,password,command)
    child.expect(pexpect.EOF)
    print(chlid.before)

if __name__ == '__main__':
    main()
