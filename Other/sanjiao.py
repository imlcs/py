#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: sanjiao.py
#  Author: lcs
#  Mail: 15224800531@163.com 
#  Created Time: 2017-07-28 15:18:14
#########################################################################

#/usr/bin/python
# 获取一个正整数
def get_num():
	while True:
		try:
			num = int(raw_input('Pls. input a number:'))
			if(num > 0):
				return num
			else:
				print('\033[31mnumber is gt 0!\033[0m')
		except:
			print('Input Error!')
# 打印直角三角形
def zhijiao_sanjiao():
	print # 美化输出
	for i in range(1,num+1): #不加一会导致比正常输出少一行
		for j in range(1,i+1): #同上
			print('*'),
		print # 换行
# 打印正三角形
def zheng_sanjiao():
	print
	temp = int((num +1) / 2) # 先找到中点位置的值
	i = j = temp
	for m in range(1,temp+1): # 正三角形输出行数是正常输出的一半多一
		for n in range(1,num+1): # 从中点向两边依次打印，在 i 和 j 范围内的打印 * 号，不在的打印空格
			if (i <= n <= j):
				print('*'),
			else:
				print(' '),
		i = i - 1
		j = j + 1
		print # 换行

def init():
	global num 
	num = get_num()
	zhijiao_sanjiao()
	if(num % 2 == 1):
		zheng_sanjiao()

init()
