#!/usr/bin/python
# coding: utf-8

"""
大根堆的实现
"""


class MyHeap(object):
    def __init__(self, iterable=None, large_top=True):
        self.large_top = large_top
        if not iterable:
            self.data = []
        else:
            self.data = list(iterable)
            n = len(iterable)
            for i in range((n//2)-1,-1,-1):
                self._xialv(i)        
        
    def _parent(self, index):
        return (index-1) // 2

    def _lchild(self, index):
        return index * 2 + 1

    def _rchild(self, index):
        return (index + 1) * 2

    def __repr__(self):
        return `self.data`

    def __str__(self):
        return repr(self.data)

    def __len__(self):
        return len(self.data)

    def heappop(self):  
        res = self.data[0]
        if len(self.data) > 1:
            self.data[0] = self.data.pop()
        self._xialv(0)
        return res

    def heapappend(self, item):
        self.data.append(item)
        self._shanglv()

    def _shanglv(self):
        i = len(self.data) - 1
        while i != 0:
            j = self._parent(i)
            if self.large_top:
            # 构造大根堆， 父节点的值不小于子节点的值
                if self.data[i] > self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                    i = j
                else:
                    break
            else:
                # 小根堆
                if self.data[i] < self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                    i = j
                else:
                    break

    def _xialv(self, index):
        i = index
        while self.__have_childe(i):
            lc = self._lchild(i)
            rc = self._rchild(i)
            if self.large_top:
                # 大根堆
                # 为了应对 lc 是 self.data最后一个元素
                if rc < len(self.data):
                    large_one = lc if self.data[lc] > self.data[rc] else rc
                else:
                    large_one = lc
                if self.data[i] >= self.data[large_one]:
                    break
                else:
                    self.data[i], self.data[large_one] = self.data[large_one], self.data[i]
                    i = large_one
            else:
                # 小根堆
                if rc < len(self.data):
                    small_one = lc if self.data[lc] < self.data[rc] else rc
                else:
                    small_one = lc
                if self.data[i] < self.data[small_one]:
                    break
                else:
                    self.data[i], self.data[small_one] = self.data[small_one], self.data[i]
                    i = small_one

    def __have_childe(self, i):
        rc = self._rchild(i)
        lc = self._lchild(i)
        if rc < len(self.data):
            return True
        else:
            if lc < len(self.data):
                # 这种情况就是 rc刚好==len(self.data) ,lc就是最后一个元素的index
                return True
            return False

    def get_top(self):
        return self.data[0]



if __name__ == '__main__':
    a = [4,3,2,1,5,10,22]
    heap_a = MyHeap(a,False)
    print heap_a
    for i in range(len(heap_a)):
        print heap_a.heappop()
    print '-'*20
    a = [4,3,2,1,5,10,22]
    heap_a = MyHeap(a)
    print heap_a
    for i in range(len(heap_a)):
        print heap_a.heappop()






