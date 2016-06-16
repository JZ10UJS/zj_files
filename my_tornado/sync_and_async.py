#!/usr/bin/python
# coding: utf-8


import sys

from tornado import gen
from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado.concurrent import Future
from tornado.ioloop import IOLoop 


def synchronous_fetch(url):
    http_client = HTTPClient()
    rsp = http_client.fetch(url)
    return rsp.body


def asynchronous_fetch(url, callback=lambda rsp:rsp.body):
    http_client = AsyncHTTPClient()
    def handle_rsp(rsp):
        return callback(rsp)
    http_client.fetch(url, callback=handle_rsp)


def async_fetch_future(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    fetch_future.add_done_callback(
        lambda f: my_future.set_result(f.result()))
    return my_future


@gen.coroutine
def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    rsp = yield http_client.fetch(url)
    raise gen.Return(rsp.body)


if __name__ == '__main__':
    url = 'http://www.huxiu.com/article/147694/1.html?f=column_feed_article'
    a = synchronous_fetch(url)
    print type(a)
    b = IOLoop.current().run_sync(lambda :asynchronous_fetch(url))
    print type(b)
    c = async_fetch_future(url)
    print type(c)

    # run_sync 不接受参数，所以要用lambda包住
    d = IOLoop.current().run_sync(lambda :fetch_coroutine(url))
    print type(d), len(d)