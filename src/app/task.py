import threading

import pytest
import os
import schedule
import time
from common.utils.mailwithzip import mailwithzip


def job1A():
    os.system('start1.bat')
    pytest.main(['-s', '-q', 'test_pushImageNew.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config1'])
    os.system('allure generate report -o /html --clean')


def job1B():
    os.system('start2.bat')
    pytest.main(['-s', '-q', 'test_pushImageNew.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config2'])
    os.system('allure generate report -o /html --clean')


def job2A():
    # os.system('python test_openchrome.py')
    os.system('start1.bat')
    pytest.main(['-s', '-q', 'test_videoNew.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config1'])
    os.system('allure generate report -o /html --clean')


def job2B():
    # os.system('python test_openchrome.py')
    os.system('start2.bat')
    pytest.main(['-s', '-q', 'test_videoNew.py', '--clean-alluredir', '--alluredir', 'report', '--configFile=config2'])
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


def threading_job_1_A():
    threading.Thread(target=job1A).start()


def threading_job_1_B():
    threading.Thread(target=job1B).start()


def threading_job_2_A():
    threading.Thread(target=job2A).start()


def threading_job_2_B():
    threading.Thread(target=job2B).start()


def threading_stop():
    threading.Thread(target=stop).start()


def threading_send_mail():
    threading.Thread(target=sendMail).start()


if __name__ == '__main__':

    # 黑屏测试
    # schedule.every().day.at("22:37").do(threading_job_1_A)
    # schedule.every().day.at("08:00").do(threading_job_1_B)
    # schedule.every().day.at("10:30").do(threading_stop)

    # 卡顿测试
    schedule.every().day.at("20:39").do(threading_job_2_A)
    # schedule.every().day.at("08:00").do(threading_job_2_B)
    schedule.every().day.at("23:55").do(threading_stop)

    # 发送邮件，上传日志
    schedule.every().day.at("23:59").do(threading_send_mail)

    while True:
        schedule.run_pending()
        time.sleep(1)
