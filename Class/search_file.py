#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: search_file.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-13 20:51:30
#########################################################################

#/usr/bin/python

import os

#path = "/home/lcs/Python"
path = '.'
def all_file(search_str):
    for roots,dirs,files in os.walk(path):
        for f in files:
            file_path = os.path.join(roots,f)
            if search_str in file_path:
                print(file_path)

if __name__ == '__main__':
    search = input('Pls. input your want search file name: ')
    all_file(search)
