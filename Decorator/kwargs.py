#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: kwargs.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-05 14:33:45
#########################################################################

#/usr/bin/python
def dicts(**kwargs):
    for tup in sorted(kwargs.items(), key = lambda sort:sort[0], reverse=False):
        print("%s\t:%s" % (tup[0], tup[1]))
    return(1)

dicts(**{'1':'zhangsan', '2':'lisi', '3':'wangwu'})
