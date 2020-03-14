import pytest
import os
import schedule
import time
from common.utils.mailwithzip import mailwithzip
import sys
from common.utils.listener import listener
import threading

def job1():
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


def job2():
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_video.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


def stop():
    listener.setStopTest('stopListener.txt', 'True');
    os.system('stop2.bat')

def buildMailContent(fujianName, contentFileName, title):
    rootPath = 'F:\\GZBAPP\\src\\app\\log\\'
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


def threading_job_1():
    threading.Thread(target=job1).start()


def threading_job_2():
    threading.Thread(target=job2).start()


def threading_stop():
    threading.Thread(target=stop).start()


def threading_send_mail():
    threading.Thread(target=sendMail).start()


def test1():
    os.system('start1.bat')
    pytest.main(['-s', '-q', 'test_pushImage1.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config1'])
    os.system('allure generate report -o /html --clean')


def test2():
    os.system('start2.bat')
    pytest.main(['-s', '-q', 'test_pushImage1.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config2'])
    os.system('allure generate report -o /html --clean')


if __name__ == '__main__':
    threading.Thread(target=test1).start()
    threading.Thread(target=test2).start()

    # schedule.every().day.at("9:00").do(threading_job_1)
    #
    # schedule.every().day.at("12:00").do(threading_stop)
    #
    # schedule.every().day.at("12:05").do(threading_job_2)
    #
    # schedule.every().day.at("17:28").do(threading_stop)
    #
    # schedule.every().day.at("17:30").do(threading_send_mail)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
