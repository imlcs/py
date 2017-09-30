#########################################################################
#  -*- coding:utf-8 -*-  
#  File Name: flaskapp.py
#  Author: lcs
#  Mail: liuchengsheng95@qq.com
#  Created Time: 2017-09-26 14:20:57
#########################################################################

#/usr/bin/python

from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')

@flask_app.route('/hello')

def hello_world():
    return Response(
        "Hello world from Flask!\n",
        mimetype='text/plain'
    )
app = flask_app.wsgi_app