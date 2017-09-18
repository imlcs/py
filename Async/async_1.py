#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: async_1.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-17 11:16:44
#########################################################################

#/usr/bin/python

import time

import asyncio

now = lambda:time.time()

async def do_some_walk(x):
    print('Watting: ', x)

start = now()

coroutine = do_some_walk(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)
