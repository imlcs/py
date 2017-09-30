#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: app.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-14 20:08:47
#########################################################################

#/usr/bin/python

import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

from jinja2 import Environment, FileSystemLoader
from config import configs
import orms
'''
def index(request):
    return web.Response(body=b'<h1>Hello World!</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'',80)
    logging.info('Server started at 0.0.0.0:80...')
    return srv
'''

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
