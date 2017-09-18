#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: async_3.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-17 19:34:59
#########################################################################

#/usr/bin/python

import asyncio
 
import time
 
now = lambda: time.time()
 
async def do_some_work(x):
    print('Waiting: ', x)
 
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)
async def main(): 
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
 
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # dones,pendings = await asyncio.wait(tasks)
    return await asyncio.gather(*tasks)
 
 
start = now()
 
loop = asyncio.get_event_loop()
try:
    results = loop.run_until_complete(main())
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
for result in results:
    print('Task ret: ', result)

print('TIME: ', now() - start)
