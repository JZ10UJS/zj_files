#!usr/bin/python
# coding:utf-8

from wsgiref.simple_server import make_server

def application(evn, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (evn['PATH_INFO'][1:] or 'World')

httpd = make_server('', 8080, application)
print 'Serving HTTP on port 8080...'

httpd.serve_forever()

