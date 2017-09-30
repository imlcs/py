#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: webserver2.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-25 16:31:25
#########################################################################

#/usr/bin/python

import socket

from io import StringIO

import sys, subprocess


class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )

        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        host,port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def server_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024).decode()

        print('< Request')
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.rstrip('\r\n').splitlines()
        ))
        self.parse_request(request_data)
        env = self.get_environ()
        result = self.application(env, self.start_response)
        self.finish_response(result)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        (
            self.request_method,
            self.path,
            self.request_version,
        ) = request_line.split()

    def get_environ(self):
        env = {}
        env['wsgi.version'] = (1,0)
        env['wsgi.url_scheme'] = 'http'
        env['wsgi.input'] = StringIO(self.request_data)
        env['wsgi.error'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once'] = False
        env['REQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT'] = str(self.server_port)
        return env

    def start_response(self, status, response_headers, exc_info = None):
        server_headers = [
            ('Date', subprocess.getoutput('date')),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]

    def finish_response(self,result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}:{1}\r\n'.format(*header)
            response += '\r\n'
            print(type(result))
            print(type(response))
            print(result)
            for data in result:
                print(type(data))
                response += data.decode()

            print('< Response')
            print(''.join(
                '< {line}\r\n'.format(line=line)
                for line in response.split('\r\n')
            ))
            self.client_connection.sendall(bytes(response,encoding='utf8'))
        finally:
            self.client_connection.close()

SERVER_ADDRESS = (HOST, PORT) = '',80
def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as modult:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port}...\n'.format(port=PORT))
    httpd.server_forever()
