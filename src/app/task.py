import pytest
import os
import schedule
import time


class DoTask:

    def job(self, folderName):
        pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
        #os.system('allure generate report/ -o report/html --clean')
        os.system('allure generate ' + folderName + '/ -o ' + folderName + '/html --clean')


doTask = DoTask()

if __name__ == '__main__':
    time1 = "17:23"
    time2 = "17:26"

    # 第一轮
    schedule.every().day.at(time1).do(doTask.job('report1'))

    # 第二轮
    schedule.every().day.at(time2).do(doTask.job('report2'))

    while True:
        schedule.run_pending()
        time.sleep(1)
