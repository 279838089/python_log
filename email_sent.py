#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class EmailSent(object):
    def __init__(self, from_email, password, smtp_server, smtp_prot):
        self.from_email = from_email
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_prot = smtp_prot

    def sent_emails(self, to_email, title, content):
        if content is not None and content != '':
            try:
                msg = MIMEText(content, 'plain', 'utf-8')
                msg['From'] = Header(title, 'utf-8').encode()
                msg['To'] = Header('管理员', 'utf-8').encode()
                msg['Subject'] = Header('来自%s ' % title, 'utf-8').encode()
                server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_prot)
                server.set_debuglevel(1)
                server.login(self.from_email, self.password)
                server.sendmail(self.from_email, to_email, msg.as_string())
                return 1
            except smtplib.SMTPException as e:
                print(e)
                # print('邮件发送失败')
                return 2

            finally:
                # 退出SMTP服务器
                server.quit()
        else:
            # print('没内容所以没发送邮件')
            return 3

# mails = EmailSent('279838089@qq.com', 'rxojdkpncijubgeb' , 'smtp.qq.com', 465)
# mails.sent_emails(['saier@sain3.com', '279838089@qq.com'], '1', 'hello saier')
