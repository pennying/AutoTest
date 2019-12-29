import schedule
import time
import pytest
import os
from src.app.test_pushImage import testTXTS


class Schedule(object):

    def test_job(self):
        testTXTS.test_txts()

    schedule.every().day.at("18:00").do(test_job)
    while True:
        schedule.run_pending()
    time.sleep(1)


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'schedule.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report/ -o report/html --clean')

