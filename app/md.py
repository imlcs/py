#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: md.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2018-05-29 14:18:33
#########################################################################

#/usr/bin/python
import hashlib          
text = "123456"
md5_object = hashlib.md5()
md5_object.update("123456")
print md5_object.hexdigest()   

m = hashlib.md5()
m.update("123456")
print m.hexdigest()
