#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
处理用户指定目录下的所有py文件，
记录各项数据，并且输出到txt文件或csv文件中
"""

import os
import sys
import keyword

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class HandPy(object):
    """处理一个py文件的详细内容"""
    def __init__(self, file_path):
        self.path = file_path
        self.root = os.path.split(file_path)[0]
        self.name = os.path.split(file_path)[1]
        self.lines = 0
        self.kw_dict = {}
        self.comments = 0
        self.blocks = 0
        
    def count_lines(self):
        with open(self.path) as f:
            for line in f:
                if line.strip():
                    self.lines += 1

    def count_comments(self):
        with open(self.path) as f:
            self.comments = 0
            for line in f:
                if line.strip().startswith('#'):
                    self.comments += 1

    def count_kws(self):
        kw_list = keyword.kwlist  # python保留字
        self.kw_dict = {}
        with open(self.path) as f:
            contents = f.read()
        self.blocks = contents.count(':')
        for item in kw_list:
            item_count = contents.count(item)  # 获得该py文档中，该关键词出现多少次
            if item_count:
                self.kw_dict[item] = item_count

    def write_to_txt(self):
        self.count_lines()
        self.count_comments()
        self.count_kws()
        format = '%s'+' %d'*9 +'\n'
        print 'writing %s ....' % self.path
        txt_f = open(os.path.join(BASE_DIR,'zhangjie.txt'), 'a')   # 在当前文件目录下创建txt
        txt_f.writelines(format % (self.name, self.lines, self.comments, self.kw_dict.get('def',0),
                                   self.blocks, self.kw_dict.get('for',0), self.kw_dict.get('while',0),
                                   self.kw_dict.get('if',0), len(self.kw_dict), sum(self.kw_dict.values())
                                   )
                        )
        txt_f.close()


class HandPath(object):
    """获取指定path下的所有py文件的路径"""
    def __init__(self, path):
        self.q = []
        self.get_pyfile_list(path)

    def add_pyfile_in_list(self, path):
        file_dir_list = os.listdir(path) # 获取该path下的所有files, dirs
        for file_dir in file_dir_list:
            f_d_path = os.path.join(path, file_dir)
            if os.path.isdir(f_d_path):
                self.add_pyfile_in_list(f_d_path)
            else:
                if file_dir.endswith('.py'):
                    self.q.append(f_d_path)

    def go(self):
        while self.q:
            pyfile_path = self.q.pop()
            a = HandPy(pyfile_path)
            a.write_to_txt()


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        try:
            path = raw_input('Enter the path: ')
        except (KeyboardInterrupt, EOFError), e:
            path = ""

    if not os.path.isdir(path):
        return

    hand = HandPath(path)
    hand.go()
    print '\nDONE!'


if __name__ == '__main__':
    main()