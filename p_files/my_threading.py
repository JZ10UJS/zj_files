#!/usr/bin/python
# coding: utf-8


import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        print 'I am thread %s at time %s' % (self.name, time.time())


def main():
    for i in range(5):
        my_thread = MyThread()
        my_thread.run()


if __name__ == '__main__':
    main()
