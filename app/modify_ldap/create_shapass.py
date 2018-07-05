#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: modify_ldap/create_shapass.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-05-29 14:56:24
#########################################################################

#/usr/bin/python

import pexpect,sys
pw = sys.argv[1]
pw = pw + '\n'

pexpect.run('slappasswd', events={
    "New password:": pw,
    "Re-enter new password:": pw
    },logfile=sys.stdout)
