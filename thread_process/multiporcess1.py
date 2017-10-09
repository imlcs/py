#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: multiporcess1.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-13 21:41:04
#########################################################################

#/usr/bin/python

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
