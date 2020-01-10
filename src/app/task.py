import pytest
import os
import schedule
import time


def job():
    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')


if __name__ == '__main__':

    schedule.every().day.at("09:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
