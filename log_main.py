#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import email_sent
import io_read
from time import gmtime, strftime

class LogMain(object):
    def __init__(self, from_email, password, smtp_server, smtp_prot):
        self.email_sent = email_sent.EmailSent(from_email, password, smtp_server, smtp_prot)
        self.io_read = io_read.IoRead()

    def log(self, url1, url2, to_email, title):
        try:
            # 读取两个文件的内容,第二个文件才是增加内容的文件
            file_content1 = self.io_read.get_file(url1)
            file_content2 = self.io_read.get_file(url2)
            # 比较两个文件的差异
            diff = self.io_read.diff_file(file_content1, file_content2)
            # 差异发送到邮件
            hit_email = self.email_sent.sent_emails(to_email, title, diff)
            # 发邮件成功的话，要覆盖后面的文件，用于下次对比
            if hit_email == 1:
                self.io_read.copy_file(url2, url1)
                print('Sent success')
            elif hit_email == 3:
                self.io_read.copy_file(url2, url1)
                print('No sent')
            elif hit_email == 2:
                print('Sent fail')
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    a = strftime("%Y-%m-%d", gmtime())
    url2 = '/var/www/internalcsm/application/logs/log-%s.php' % a
    url1 = '/var/www/internalcsm/application/logs/python_temp'
    to_email = ['saier@sain3.com', 'allen.lai@sain3.com', '408827148@qq.com']
    title = 'Python自动监控'
    obj_log = LogMain('279838089@qq.com', '', 'smtp.qq.com', 465)
    obj_log.log(url1, url2, to_email, title)

    url4 = '/var/log/apache2/error.log'
    url3 = '/var/log/apache2/python_temp'
    obj_log.log(url3, url4, to_email, title)
