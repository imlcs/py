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

async def do_some_work(x):
    print('Watting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [ 
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]
# task = loop.create_task(coroutine)
loop = asyncio.get_event_loop()
# 使用asyncio.wait 使任务挂起
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task net: {}'.format(task.result()))
print('TIME: ', now() - start)
