#!usr/bin/python
# coding: utf-8
# 栈

class Stack():
    """由列表衍生的栈,弱爆了，还不如用list"""
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def push(self, content):
        if self.isfull():
            print 'Stack if full'
        else:
            self.stack.append(content)
            self.top += 1

    def out(self):
        if self.top != -1:
            self.top -= 1
            return self.stack.pop()
        else:
            print  'NO more content'
    
    def isfull(self):
        if self.top == self.size:
            return True
        else:
            return False

    def display(self):
        print self.stack

if __name__ == '__main__':
    s1 = Stack(2)
    s1.push('hello')
    s1.push(123)
    s1.push(11)
    s1.display()
    s1.out()
    s1.out()
    
