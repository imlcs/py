#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: webserver1.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-08-22 23:02:29
#########################################################################
import socket

HOST_PORT = ('',80)

listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
listen_socket.bind(HOST_PORT)
listen_socket.listen(1)

print('Servring HTTP on port %s ...' % HOST_PORT[1])
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024).decode()
    print(request)

    http_response = """\
HTTP/1.1 200 OK

Hello World!
"""

    client_connection.sendall(http_response.encode())
    client_connection.close()
