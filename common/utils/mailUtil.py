import smtplib
import time
from email.mime.text import MIMEText


class MailUtils(object):

    def send_mail(self, black, name):
        msg_from = 'test@mygzb.com'
        passwd = 'TEST@2288'
        receiver = [
            'y-pan@mygzb.com',
            'zt-lin@mygzb.com',
            'ky-huang@mygzb.com',
            'jl-ye@mygzb.com',
            'jq-feng@mygzb.com',
            'zr-huang@ejiahe.com',
            'jf-mai@mygzb.com',
            'xm-zhou@mygzb.com',
            'hd-wang@mygzb.com'
        ]
        msg_to = ",".join(receiver)
        subject = "图像推送黑屏告警"
        content = "告警时间：" + time.strftime('%Y-%m-%d %H:%M:%S') + "\n视频源:" + str(name) + "\n告警问题：图像推送连续出现" + str(black) + "次黑屏" + "\n告警级别：警告"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to

        s = smtplib.SMTP_SSL("smtp.mygzb.com", 465)
        try:
            s.login(msg_from, passwd)
            s.sendmail(msg_from, receiver, msg.as_string())
            # print("已发送告警邮件")
        finally:
            s.quit()

    def send_mail_static(self, name):
        msg_from = 'test@mygzb.com'
        passwd = 'TEST@2288'
        receiver = [
            'y-pan@mygzb.com',
            # 'xm-zhou@mygzb.com',
        ]
        msg_to = ",".join(receiver)
        subject = "图像推送卡顿告警"
        content = "告警时间：" + time.strftime('%Y-%m-%d %H:%M:%S') + "\n视频源:" + str(name) + "\n告警问题：图像推送画面卡顿" + "\n告警级别：警告"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to

        s = smtplib.SMTP_SSL("smtp.mygzb.com", 465)
        try:
            s.login(msg_from, passwd)
            s.sendmail(msg_from, receiver, msg.as_string())
            # print("已发送告警邮件")
        finally:
            s.quit()


mailUtils = MailUtils()
