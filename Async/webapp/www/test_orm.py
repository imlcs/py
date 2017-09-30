# -*- coding: utf-8 -*-


import orms, asyncio, sys
from models import User, Blog, Comment

async def test(loop):
    await orms.create_pool(loop=loop, user='root', host='192.168.1.11', password='123456', db='webapp')
    u = User(name='zhaoliu', email='zhaoliu@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orms.destory_pool()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
