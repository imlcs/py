#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: list.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com 
#  Created Time: 2017-07-13 13:59:37
#########################################################################

#/usr/bin/python
import os
from pathlib import Path
for roots,dirs,files in os.walk('/root'):
    #roots是目录路径，dirs是目录下的子目录，files是目录下的所有文件
    #print roots
    dirpath = Path(roots)
    for file in files:
        '''
            os.path.join 是Python2的写法，Python3 中取消这个方法，用 pathlib 模块的 Path 方法替代
        '''
        #print os.path.join(roots,file)
        print(dirpath / file)
