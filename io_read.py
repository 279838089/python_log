#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import difflib
import os


class IoRead(object):
    # 比较两个文件的差异，主要是新增的差异
    def diff_file(self, content1, content2):
        s = difflib.SequenceMatcher(None, content1, content2)
        for tag, i1, i2, j1, j2 in s.get_opcodes():
            if tag == 'insert':
                return content2[j1:j2]

    # 读取文件内容，注意，文件不能过大，内存溢出
    def get_file(self, file):
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        # 如果不存在此文件，创建一个空白文件
        else:
            f = open(file, 'w')
            f.close()

    # 复制文件,文件1复制给文件2
    def copy_file(self, file1, file2):
        file_content1 = self.get_file(file1)
        with open(file2, 'w') as f:
            f.write(file_content1)


'''
a = IoRead()
# print(a.diff_file('11', ''))
b=a.diff_file(a.get_file('/Applications/MAMP/htdocs/python/2.py'), a.get_file('/Applications/MAMP/htdocs/python/2.py'))
if b is not None and  b != '':
    print(1)

# print(a.get_file('/Applications/MAMP/htdocs/python/3.py'))
#a.copy_file('/Applications/MAMP/htdocs/python/2.py', '/Applications/MAMP/htdocs/python/3.py')

a = "11"
b = "1122ffds22233"
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    if tag == 'insert':
        # print('{:7}   a[{}:{}] --> b[{}:{}] {!r:>8} --> {!r}'.format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
        print(b[j1:j2])
'''
