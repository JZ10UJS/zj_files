#!/usr/bin/python
# coding: utf-8


import sys

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ['<h1>Item 1</h1>', 'Item 2', "Item 3"]
        self.render('index.html', title='Tornado', items=items)


class StoryHandler(tornado.web.RequestHandler):
    def get(self, pk):
        self.write('You looking the %s story' % pk)


class InfoHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', 'text/html')
        self.write("<html><body><form method='post'>" \
                   "<input name='message' type='text'>" \
                   "<input type='submit' value='提交'>" \
                   "</form></body></html>")

    def post(self):
        self.set_header('Content-Type', 'text/plain')
        # a居然是个列表
        a = self.request.arguments.get('message')
        self.write('You wrote: ' + self.get_argument("message"))


app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/story/(?P<pk>\d+).html', StoryHandler),
        (r'/write', InfoHandler),
    ])


if __name__ == '__main__':
    app.listen(8888)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt as e:
        sys.exit(1)
    
