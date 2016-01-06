#!usr/bin/python
# coding: utf-8

import random, time, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def f1():
    return task_queue

def f2():
    return result_queue

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=f1)
QueueManager.register('get_result_queue', callable=f2)

manager = QueueManager(address=('192.168.1.106', 5000), authkey='abc')


def communicate():
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    while True:
        try:
            r = result.get(timeout=10)
        except Queue.Empty:
            print 'result queue is empty.'
            break
        else:
            print('Result: %s' % r)

    manager.shutdown()

if __name__ == '__main__':
    freeze_support()
    manager.start()
    communicate()
