# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Mailwithzip(object):

    def send_mail(self, zipFilePath, zipFile, mailText):
        fromaddr = 'test@mygzb.com'
        password = 'TEST@2288'

        receiver = [
            'y-pan@mygzb.com',
            # 'xm-zhou@mygzb.com',
            # 'jf-mai@mygzb.com'

        ]
        toaddrs = ",".join(receiver)

        content = mailText
        textApart = MIMEText(content)

        zipApart = MIMEApplication(open(zipFilePath, 'rb').read())
        zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

        m = MIMEMultipart()
        m.attach(textApart)
        m.attach(zipApart)
        m['Subject'] = '图像推送自动化测试报告'

        try:
            server = smtplib.SMTP_SSL("smtp.mygzb.com", 465)
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print('error:', e)  # 打印错误


mailwithzip = Mailwithzip()
