#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: readline.py
#  Author: lcs
#  Mail: 15224800531@163.com 
#  Created Time: 2017-07-28 15:04:57
#########################################################################

#/usr/bin/python
f = open('rpm.log','r')
for line in f.readlines():
	print(line),

f.close()
