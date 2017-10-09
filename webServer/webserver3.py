#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: webserver3.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-27 09:55:27
#########################################################################

#/usr/bin/python

import socket
import  time

SERVER_ADDRESS = (HOST, PORT) = '',80
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""
HTTP/1.1 200 OK

Hello, World!
"""

    client_connection.sendall(http_response)
    time.sleep(30)


def server_forever():
    listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {}...'.format(PORT))

    while True:
        client_connection,client_address = listen_socket.accept()
        print(client_address)
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    server_forever()