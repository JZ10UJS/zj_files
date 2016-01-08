#!/usr/bin/python
# coding: utf-8

import re
import os
import xlwt

try:
    # 这个要自己把淘宝页面代码，复制下来
    f = open('d:/test.txt','r')
except IOError, e:
    print 'no such file'
else:
    s = f.read()
    f.close()
    r_l = r'\"raw_title\":\"(.+?)\".+?\"view_price\":\"(.+?)\".+?\"reserve_price\":\"(.+?)\".+?\"view_sales\":\"(.+?)\".+?\"comment_count\":\"(.+?)\".+?\"nick\":\"(.+?)\"'
    l = re.findall(r_l, s)
    workbook = xlwt.Workbook()
    ws = workbook.add_sheet('name1')
    ws_title = [u'标题',u'售价',u'原价',u'销量',u'评论数',u'店铺']
    for i in range(len(ws_title)):
        ws.write(0,i,ws_title[i])
        
    for i in range(len(l)):
        for j in range(len(l[i])):
            ws.write(i+1, j, l[i][j].decode('gbk'))

    workbook.save('e:/1.xls')
    a = raw_input('Mission Accomplished')
