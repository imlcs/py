#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: aio_web.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-14 19:46:03
#########################################################################

#/usr/bin/python

from aiohttp import web
import asyncio

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>Hello %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('UTF-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/{name}',hello)
    srv = await loop.create_server(app.make_handler(),'',80)
    print('Server started at http://0.0.0.0:80...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
