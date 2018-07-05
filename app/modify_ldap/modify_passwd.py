#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: modify_ldap/create_shapass.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-05-29 14:56:24
#########################################################################

#/usr/bin/python

import pexpect,sys

pexpect.run('ldapmodify -x -D cn=Manager,dc=kqc,dc=cc -W -H "ldap://127.0.0.1:389/" -f ./modify_ldap/modifypass.ldif ', events={
    "Enter LDAP Password:": '123456\n'
    })
