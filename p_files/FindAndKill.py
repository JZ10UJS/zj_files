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


def del_file_if(l, string, path):
    """
    如果列表l中的某项元素含有特定字符串string,则删除该元素，并打印新列表
    """
    s = copy.copy(l)
    for index, file_name in enumerate(l):
        if string in file_name:
            os.remove(os.path.join(path, l[count]))
    print u"名字中含有'f'的文档已被删除，不包括文件夹！"


def del_folder_if(var_path,str1):
    """
    如果路径中含有字符串str1,删除该路径及其下属文件
    """
    if str1 in var_path:
        shutil.rmtree(var_path)
  

def main():
    disk = raw_input(u'请输入盘符:')
    folder_name = raw_input(u'请输入文件夹名不能含有的字符:')
    file_name = raw_input(u'请输入文档名不能含有的字符:')

    for path, d, filename in os.walk(disk+':\\'):
        print path, filename
        deldirif(path,f_name) #先walk一遍，将名称中含有fl的文件夹 将被删除
        
    for path, d, filename in os.walk(disk+':\\'):
        delSthif(filename,doc_name,path) #再walk一遍，将名称中含有f的文档，将被删除

    print "Mission Accomplished!"
    


