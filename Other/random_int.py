#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: random.py
#  Author: lcs
#  Mail: 15224800531@163.com 
#  Created Time: 2017-07-28 16:31:03
#########################################################################

#/usr/bin/python
import random

num = random.randint(1,100)
while True:
	try:
		input_num = int(raw_input('Pls. input a number(1-100):'))
		if (input_num > num):
			print('Big!')
		elif (input_num < num):
			print('Small!')
		else:
			print('Yes! This number is %d' % num)
			break
	except:
		print('Input Error!')
