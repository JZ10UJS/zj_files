#!/usr/bin/python27
# coding: utf-8

import os
import copy
import shutil
'''
def dirList(path):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if  os.path.isdir(filepath):
            dirList(filepath)
        print filepath
        
allfile = dirList('f:\\python27\\test')
'''
disk = raw_input(u'请输入盘符:')
f_name = raw_input(u'请输入文件夹名不能含有的字符:')
doc_name = raw_input(u'请输入文档名不能含有的字符:')

def delSthif(l,str1,path):  #如果列表l中的某项元素含有字符串str1,则删除该元素，并打印新列表
    s = copy.copy(l)
    count = 0
    for i in l:
        if str1 not in i:
            count += 1
        else:
            os.remove(path+'\\'+l[count])
    #print "名字中含有'f'的文档已被删除，不包括文件夹！"


def deldirif(var_path,str1):#如果路径中含有字符串str1,删除该路径及其下属文件
    if str1 in var_path:
        shutil.rmtree(var_path)
  
for path,d,filename in os.walk(disk+':\\'):
    #print path,filename
    deldirif(path,f_name) #先walk一遍，将名称中含有fl的文件夹 将被删除
for path,d,filename in os.walk(disk+':\\'):
    delSthif(filename,doc_name,path) #再walk一遍，将名称中含有f的文档，将被删除

a = raw_input("Mission Accomplished!\nPress any key to close:")
while a :
    break

    


