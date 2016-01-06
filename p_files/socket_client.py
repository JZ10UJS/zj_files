#!usr/bin/python
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.240.131', 9999))

print s.recv(1024)

for data in ['hello','this is from ', 'zhuji']:
    s.send(data)
    print s.recv(1024)

s.send('exit')
s.close()
