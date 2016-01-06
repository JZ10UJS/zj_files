from multiprocessing import Process, Queue
import os, time, random

# 每0.2秒向q写数据
def write(q):
    for value in range(10):
        print 'Put (%s) to queue...' % value
        q.put(value)
        time.sleep(0.2)

# 每0.3秒从q读数据
def read(q):
    while True:
        try:
            value = q.get(True, 2) # 等待2秒，若没得到数据，就raise一个错误
        except:
            print 'q is empty...'
            break
        else:
            print 'Get %s from queue.' % value
            time.sleep(0.3)

# 在IDLE中，看不出过程，需要到cmd中去运行
if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
