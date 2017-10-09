#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: one.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-05 09:18:31
#########################################################################

#/usr/bin/python
import logging,functools
def use_logging(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.warn("%s in running...%s" % (func.__name__, text))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@use_logging('fdsfsdfsdfs')
def foo():
    print('Hell world!')
    #logging.warn('foo is running...')

if __name__ == '__main__':
    foo()
