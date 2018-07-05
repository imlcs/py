#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: create_ldap_userfile.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-05-23 23:08:26
#########################################################################

#/usr/bin/python

import sys
reload(sys)
import os
sys.setdefaultencoding('utf-8')
from pypinyin import pinyin, lazy_pinyin
os.system("echo > gitlab_user.ldif")
ldap_usefile=open('gitlab_user.ldif','w+')
ldap_usefile.write('\n')

# 每次添加用户时 number 手动加 100
number = 1130
with open('./useradd.txt','r') as f:
    userinfo = f.readlines()
    for item in userinfo:
        user = item.split(' ')[0]
        username = item.split(' ')[0].decode('utf-8').encode('unicode_escape')
        pinyin_username = (''.join(lazy_pinyin(username.decode('unicode-escape'))))
        email = item.split(' ')[1]

        ldap_usefile.write("dn: uid=")
        ldap_usefile.write(pinyin_username)
        ldap_usefile.write(",ou=gitlab,dc=kqc,dc=cc\n")

        ldap_usefile.write("objectClass: inetOrgPerson\nobjectClass: posixAccount\nobjectClass: shadowAccount\n")

        ldap_usefile.write("uid: ")
        ldap_usefile.write(pinyin_username)
        ldap_usefile.write("\n")

        ldap_usefile.write("cn: ")
        ldap_usefile.write(user)
        ldap_usefile.write("\n")

        ldap_usefile.write("sn: ")
        #ldap_usefile.write(username.decode('unicode-escape')[1:].encode('unicode-escape').decode('string_escape'))
        ldap_usefile.write(username.decode('unicode-escape')[1:])
        ldap_usefile.write("\n")

        ldap_usefile.write("givenName: ")
        ldap_usefile.write(username.decode('unicode-escape')[0:1])
        ldap_usefile.write("\n")

        ldap_usefile.write("mail: ")
        ldap_usefile.write(email)
        ldap_usefile.write("\n")

        ldap_usefile.write("userPassword: {SSHA}arBWn7LDfvwT5U2NqDnczT5ROTqM6AlO\n")

        ldap_usefile.write("loginShell: /bin/bash\n")

        ldap_usefile.write("uidNumber: ")
        ldap_usefile.write(str(number))
        ldap_usefile.write("\n")

        ldap_usefile.write("gidNumber: ")
        ldap_usefile.write(str(number))
        ldap_usefile.write("\n")

        ldap_usefile.write("homeDirectory: /home/users/")
        ldap_usefile.write(pinyin_username)
        ldap_usefile.write("\n")

        ldap_usefile.write("\n")
        number += 1 
ldap_usefile.close()
