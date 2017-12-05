#!/usr/bin/env python
# coding=utf-8

from templite import Templite
# Make a Templite object.
templite = Templite('''
<h1>Hello {{name|upper}}!</h1>
{% for topic in topics %}
    {% if topic == "LINUX" %}
    <p>You are interested in {{topic|lower}}.</p>
    {% endif %}
{% endfor %}
{% for d in D %}
                    <p>{{ d.name }} : {{ d.age }}</p>
{% endfor %}
''',
{'upper': str.upper},
{'lower': str.lower},
)

text = templite.render({
    'name': "J.am",
    'topics': ['python', 'Geometry', 'Juggling', 'LINUX'],
    'D':({'name':'zhangsan','age':24},{'name':'lisi','age':54})
})
