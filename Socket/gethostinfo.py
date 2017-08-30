#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: gethostinfo.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-08-23 22:57:49
#########################################################################

#/usr/bin/python
import socket

def get_host_info():
	host_name = socket.gethostname()
	ip_addr = socket.gethostbyname(host_name)

	host_info = [host_name, ip_addr]
	return host_info

if __name__ == '__main__':
	print(get_host_info())
