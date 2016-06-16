#!/usr/bin/python
# coding: utf-8


import threading


local_data = threading.local()
local_data.name = 'local_data'


class TestThread(threading.Thread):
    def run(self):
        print threading.currentThread()
        print local_data.__dict__
        local_data.name = self.getName()
        local_data.add_by_sub_thread = self.getName()
        print local_data.__dict__


if __name__ == "__main__":
    print threading.currentThread()
    print local_data.__dict__
    print 
    t1 = TestThread()
    t1.start()
    t1.join()
    print 
    t2 = TestThread()
    t2.start()
    t2.join()
    print 
    print threading.currentThread()
    print local_data.__dict__
