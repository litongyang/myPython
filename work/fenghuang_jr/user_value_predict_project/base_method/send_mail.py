# __author__ = 'lty'
# -*- coding: utf-8 -*-

# __author__ = 'lty'
# -*- coding: utf-8 -*-
'''
发送txt文本邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''
import smtplib
from email.mime.text import MIMEText
import read_conf as read_conf

mail_tolist_1 = read_conf.ReadConf().get_options("mail_send", "mail_tolist")
mail_host_1 = read_conf.ReadConf().get_options("mail_send", "mail_host")
mail_user_1 = read_conf.ReadConf().get_options("mail_send", "mail_user")
mail_password_1 = read_conf.ReadConf().get_options("mail_send", "mail_password")
mail_postfix_1 = read_conf.ReadConf().get_options("mail_send", "mail_postfix")


def send_mail(to_list, host, username, password, mail_postfix, sub, content):
    to_list = to_list.split(',')
    me = "hello" + "<" + username + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(host, 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

""" test """
if __name__ == '__main__':
    if send_mail(mail_tolist_1, mail_host_1, mail_user_1, mail_password_1, mail_postfix_1, "hello", "hello world!"):
        print "发送成功"
    else:
        print "发送失败"