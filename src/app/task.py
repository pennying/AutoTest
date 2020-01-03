import pytest
import os
import schedule
import time


def job():
    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


if __name__ == '__main__':

    time1 = "09:00"
    schedule.every().day.at(time1).do(job)
    time2 = "11:30"
    schedule.every().day.at(time2).do(job)
    time3 = "14:00"
    schedule.every().day.at(time3).do(job)
    time4 = "16:30"
    schedule.every().day.at(time4).do(job)
    time5 = "19:00"
    schedule.every().day.at(time5).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
