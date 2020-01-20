import pytest
import os
import schedule
import time
from common.utils.mailwithzip import mailwithzip


def job1():
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


def job2():
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_video.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


def stop():
    os.system('stop.bat')


def buildMailContent(fujianName, contentFileName, title):
    rootPath = 'D:\\GZBAPP\\src\\app\\log\\'
    today = time.strftime('%Y-%m-%d').replace('-', '')
    readTextName = contentFileName + today + '.txt'
    readTextPath = rootPath + readTextName
    f_read = open(readTextPath, "r+")
    content = f_read.readlines()

    sum = int(content[1].replace('\n', ''))
    black = int(content[2].replace('\n', ''))

    data = [
        title + '\n',
        '总执行数:' + str(sum),
        '失败次数:' + str(black),
        '失败率为:' + str(black / sum)
    ]

    content = "\n".join(str(i) for i in data)

    fujianName = fujianName + today + '.txt'
    fujianPath = rootPath + fujianName
    mailwithzip.send_mail(
        fujianPath,
        fujianName,
        content
    )


def sendMail():
    fujianName1 = 'black_screen_log_'
    contentFileName1 = 'black_screen_report_'
    fujianName2 = 'kadun_log_'
    contentFileName2 = 'kadun_report_'
    buildMailContent(fujianName1, contentFileName1, '图像推送黑屏测试报告')
    buildMailContent(fujianName2, contentFileName2, '图像推送卡顿测试报告')


if __name__ == '__main__':

    schedule.every().day.at("20:23").do(job1)

    schedule.every().day.at("20:25").do(job2)

    schedule.every().day.at("17:31").do(sendMail)

    while True:
        schedule.run_pending()
        time.sleep(1)
