#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: yanghui.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-06 22:44:26
#########################################################################

#/usr/bin/python
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x] + L[x+1] for x in range(len(L)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 12:
        break
