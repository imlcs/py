#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: wsgiapp.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-26 16:26:46
#########################################################################

#/usr/bin/python

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type','text/plain')]
    start_response(status,response_headers)
    data = ['Hello world from a simple WSGI application']
    return data.encode()