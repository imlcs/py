#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: one.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-05 09:18:31
#########################################################################

#/usr/bin/python
import logging, logging.config
logging.config.fileConfig("./logging.conf")
logger_name = "example"
logger = logging.getLogger(logger_name)

def use_logging(func):
    logging.basicConfig(level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info("%s in running..." % func)
        return func(*args, *kwargs)
    return wrapper

@use_logging
def foo():
    print('Hell world!')
    #logging.warn('foo is running...')

if __name__ == '__main__':
    foo()
