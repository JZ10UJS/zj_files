#!/usr/bin/python
# coding: utf-8


import Queue, threading, os, shutil

import requests, urllib
from BeautifulSoup import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    
    }
task_queue = Queue.Queue()

lock = threading.Lock()
count = 0

file_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),'webpic')
if os.path.exists(file_dir):
    shutil.rmtree(file_dir)
os.mkdir(file_dir)


def getHtml(url):
    print 'connecting to the `%s`' % url
    response = requests.get(url, headers=HEADERS)
    html = response.content
    print 'connecting Success...\n'
    return html

'''
def savePicFromLinks(links):
    for index, link in enumerate(links):
        filename = 'e:/webpic/%s.jpg' % index
        print 'writing the %03d pic... by thread %s' % (index+1, self.name)
        r = requests.get(link, headers=HEADERS, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
'''


def getPicLinks(html):
    print 'getting the pic links...'
    my_soup = BeautifulSoup(html)
    tag_links = my_soup.findAll('img')
    links = map(lambda x: x.get('src'), tag_links)
    print 'Total find %d Pics' % len(links)
    print 'getting Success...\n'
    return links
    

class MyThread(threading.Thread):
    def __init__(self, lock, queue):
        super(MyThread, self).__init__()
        self.lock = lock
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            self.lock.acquire() # only for count and name the picture
            global count
            count += 1
            filename = os.path.join(file_dir, '%s.jpg' % count)
            print 'writing the %03d pic... by thread %s' % (count, self.name)
            link = self.queue.get()
            self.lock.release()
            try:
                r = requests.get(link, headers=HEADERS, stream=True, timeout=10)
            except requests.ConnectionError, e:
                print 'can not get this picture', 
                self.queue.task_done()
                continue
            else:
                if r.status_code == 200:
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(1024):
                            f.write(chunk)
                self.queue.task_done()
        


def main():
    url = raw_input('Enter the URL: ')
    html = getHtml(url)
    links = getPicLinks(html)
    for link in links:
        if link:
            task_queue.put(link)
        
    for i in range(5):
        my_thread = MyThread(lock, task_queue)
        my_thread.setDaemon(True)
        my_thread.start()
        
    task_queue.join()
    raw_input('Done!\nPress any key to Quit...')
    

if __name__ == '__main__':
    main()
