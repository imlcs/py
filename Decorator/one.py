#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: one.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-05 09:18:31
#########################################################################

#/usr/bin/python
import logging, time
def use_logging(func):
    logging.basicConfig(level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("%s: %s in running..." % (time.strftime('%F %T', time.localtime()), func.__name__))
        return func(*args, *kwargs)
    return wrapper

@use_logging
def foo():
    print('Hell world!')
    #logging.warn('foo is running...')

if __name__ == '__main__':
    foo()
