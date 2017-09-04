#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter – 1
import socket
def get_remote_machine_info():
	remote_host = 'www.baidu.com'
	try:
            print("IP is: %s" % socket.gethostbyname(remote_host))
	except socket.error as m:
	    print("%s" % (m))
if __name__ == '__main__':
	get_remote_machine_info()
