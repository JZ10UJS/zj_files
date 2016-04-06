#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

from_addr ='foo@163.com'
password = 'foobarpass'
smtp_server = 'smtp.163.com'

to_addr = raw_input('To eamil: ')
content = "<html><body><a href='http://www.baidu.com'>hello</a></body></html>"

my_msg = MIMEMultipart()
my_msg['From'] = from_addr
my_msg['Subject'] = 'Test from Python' # 邮件主题
my_msg['To'] = to_addr
my_msg['Date'] = formatdate(localtime=True)
msg = MIMEText(content, 'html', 'utf-8')
my_msg.attach(msg)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], my_msg.as_string())
server.quit()
