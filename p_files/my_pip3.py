#!usr/bin/python
# coding:utf-8

import poplib
from email.parser import Parser

eamil = 'foo@163.com'
password = 'foobar'
pop3_server = 'pop3.163.com'

server = poplib.POP3(pop3_server)

print server.getwelcome()

server.user(eamil)
server.pass_(password)

print 'Messages: %s. Size: %s' % server.stat()

resp, mails, octets = server.list()

print mails

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = '\r\n'.join(lines)

msg = Parser().parsestr(msg_content)

server.quit()
