#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: md5.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-05-29 10:52:07
#########################################################################

#/usr/bin/python
import hashlib  
  
m= hashlib.md5()  #创建md5对象  
m.update('abcdefg') #生成加密串，其中password是要加密的字符串  
print m.hexdigest()  #打印经过md5加密的字符串  
