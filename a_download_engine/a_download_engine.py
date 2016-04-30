#/usr/bin/python
# coding: utf-8


import requests
import threading
from Queue import Queue


class Downloader(object):

    def __init__(self, url):
        self.url = url
        self.thread_num = 8
        self.name = self.url.split('/')[-1]

        rsp = requests.head(self.url)
        self.total = int(rsp.headers['Content-Length'])
        print 'total is %s' % (self.total)

    def get_range(self):
        ranges = []
        offset = int(self.total/self.thread_num)
        for i in range(self.thread_num):
            if i == self.thread_num - 1:
                # 最后一个将剩下的数据全部取回, 第二个参数不指定位置
                ranges.append((i*offset, ''))
            else:
                ranges.append((i*offset, (i+1) * offset))
        # 比如content-length = 50, thread_num = 4, 所以offset = 12
        # 那么ranges [(0,12),(12,24),(24,36),(36,'')]
        return ranges

    def download(self, start, end):
        headers = {'Range':'Bytes=%s-%s'%(start, end)}
        rsp = requests.get(self.url, headers=headers)
        print '%s:%s download success!' % (start, end)
        self.fd.seek(start)
        self.fd.write(rsp.content)
        
    def run(self):
        self.fd = open(self.name, 'wb')
        thread_list = []
        n = 0
        for ran in self.get_range():
            start, end = ran
            print 'thread %d start: %s, end: %s' % (n, start, end)
            n += 1
            thread = threading.Thread(target=self.download, args=(start,end))
            thread.start()
            thread_list.append(thread)
        for i in thread_list:
            i.join()
        print 'download %s laod success!' % (self.name)
        self.fd.close()


class MyDownloader(threading.Thread):
    def __init__(self, url, queue, lock, total, fileobj):
        super(MyDownloader, self).__init__()
        self.queue = queue
        self.url = url
        self.lock = lock
        self.total = total
        self.file = fileobj
        

    def run(self):
        while not self.queue.empty():
            # 获取下载的range信息
            start, end = self.queue.get()
            headers = {'Range':'Bytes=%s-%s' % (start, end)}
            rsp = requests.get(self.url, headers=headers)
            print '%s:%s download success!' % (start, end)
            
            self.lock.acquire()
            self.file.seek(start)
            self.file.write(rsp.content)
            self.lock.release()
            
            self.queue.task_done()


if __name__ == '__main__':
    lock = threading.Lock()
    queue = Queue()
    url = 'http://dldir1.qq.com/qqfile/qq/QQ8.2/17724/QQ8.2.exe'
    rsp = requests.head(url)
    total = int(rsp.headers['Content-Length'])
    print 'total is %s' % (total)
    name = url.rsplit('/')[-1]

    offset = 2**20
    nums = total//offset + 1
    print '共要下载 %d 次' % nums
    for i in range(nums):
        if i == nums - 1:
            # 最后一个将剩下的数据全部取回, 第二个参数不指定位置
            queue.put((i*offset, ''))
        else:
            queue.put((i*offset, (i+1) * offset))
    
    with open(name, 'wb') as f:
        for i in range(10):
            down = MyDownloader(url, queue, lock, total, f)
            down.setDaemon(True)
            down.start()    
        queue.join()
        
    print '*'*40 +'\n\nDone!\n\n' + '*'*40
                        
