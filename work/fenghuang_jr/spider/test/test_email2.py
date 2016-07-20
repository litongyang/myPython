# __author__ = 'tongyang.li'

# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'lty369963@sina.com'
receiver = 'tongyang.li@fengjr.com'
subject = 'python email test'
smtpserver = 'smtp.sina.com'
username = 'lty369963@sina.com'
password = '***'

msg = MIMEText('test','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.sina.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()