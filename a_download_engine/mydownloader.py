#!/usr/bin/python
# coding: utf-8

import threading, logging
from Queue import Queue

import requests


class MyDownloader(object):
    def __init__(self, url, chunk=2**20):
        self.url = url
        self.queue = Queue()
        self.name = self.url.rsplit('/')[-1]
        self.chunk = chunk
        self.put_ranges_to_queue()

    def put_ranges_to_queue(self):
        rsp = requests.head(url)
        total = int(rsp.headers['Content-Length'])
        print 'total is %s' % total
        times = total // self.chunk + 1
        for i in range(times):
            if i == times-1:
                self.queue.put((i*self.chunk, ''))
            else:
                self.queue.put((i*self.chunk, (i+1)*self.chunk))

    def download(self):
        while not self.queue.empty():
            start, end = self.queue.get()
            headers = {'Range': 'Bytes=%s-%s' % (start, end)}
            try:
                rsp = requests.get(self.url, headers=headers, timeout=15)
            except requests.exceptions.ConnectTimeout as e:
                print 'downlaod %s: %s fail' % (start, end)
                continue
            
            self.file.seek(start)
            self.file.write(rsp.content)
            
            self.queue.task_done()
            print '%s : %s write success!' % (start, end)

    def run(self):
        try:
            self.file = open(self.name, 'wb')
            threads = []
            for i in range(10):
                my_thread = threading.Thread(target=self.download)
                threads.append(my_thread)
                my_thread.setDaemon(True)
                my_thread.start()
            self.queue.join()
        except Exception as e:
            raise e
        else:
            print '\n\n\nDONE!\n\n'
        finally:    
            self.file.close()
        


if __name__ == '__main__':
    url = 'http://dldir1.qq.com/qqfile/qq/QQ8.2/17724/QQ8.2.exe'
    d = MyDownloader(url)
    d.run()
