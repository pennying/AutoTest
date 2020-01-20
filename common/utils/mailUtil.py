import smtplib
import time
from email.mime.text import MIMEText


class MailUtils(object):

    def send_mail(self, black, name):
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
        subject = "图像推送黑屏告警"
        content = "告警时间：" + time.strftime('%Y-%m-%d %H:%M:%S') + "\n视频源:" + str(name) + "\n告警问题：图像推送连续出现" + str(black) + "次黑屏" + "\n告警级别：警告"
        # content += '\n'
        # content += text
        self.send(subject, receiver, content)

    def send_mail_static(self, name, slowCount, text):
        receiver = [
            'y-pan@mygzb.com',
            'xm-zhou@mygzb.com'
        ]
        subject = "图像推送卡顿告警"
        content = "告警时间：" + time.strftime('%Y-%m-%d %H:%M:%S') + "\n视频源:" + str(name) + "\n告警问题：图像推送连续出现" + str(slowCount) + "次卡顿" + "\n告警级别：警告"
        content += '\n'
        content += text
        self.send(subject, receiver, content)

    def send_mail_report(self, text):
        receiver = [
            'y-pan@mygzb.com'
        ]
        subject = "每日3000次报告"
        content = text
        self.send(subject, receiver, content)

    def send(self, subject, receiver, content):
        msg_from = 'test@mygzb.com'
        passwd = 'TEST@2288'

        msg_to = ",".join(receiver)

        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to

        s = smtplib.SMTP_SSL("smtp.mygzb.com", 465)
        try:
            s.login(msg_from, passwd)
            s.sendmail(msg_from, receiver, msg.as_string())
        finally:
            s.quit()


mailUtils = MailUtils()
