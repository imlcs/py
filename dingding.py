#!/usr/bin/python3

# -*- coding: utf-8 -*-
import urllib.request
import urllib
import sys 
import json
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

token = sys.argv[1]
res = ' '.join(sys.argv[2:])
res = str(res.replace(": ", "\n"))
url = "https://oapi.dingtalk.com/robot/send?access_token=" + token
hearders = { 'Content-Type' : 'application/json' }
pdata = {'msgtype':'text','text':{'content': res}}
data = json.dumps(pdata)
data = bytes(data,'utf8')
req = urllib.request.Request(url,data,hearders)
reqp = urllib.request.urlopen(req)
