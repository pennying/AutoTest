#!/usr/bin/env python
# coding:utf-8
import os
import time
import warnings
import pytest
import tempfile
import allure
import schedule
from datetime import datetime, timedelta

from config.seleniumConfig import DriverClient
from common.utils.login_xf import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.imageAssert import ImageAssert
from common.utils.adbUtils import adbUtils
from common.utils.mailUtil import mailUtils


@allure.feature("测试图像推送")
class TestTXTS:

    # 驱动
    def setup(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver(nosingleton=True)

    # 登录
    def test_login(self):
        openAppUtil.open_app(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    # 图像推送
    @allure.story('测试图像推送')
    def test_txts(self):

        """
        计算查看高清图像时出现黑屏的概率
        """
        self.driver.find_element('xpath', "//*[@text='图像推送']").click()
        time.sleep(5)
        self.driver.find_element('xpath', "//*[@text='佳米测试']").click()

        sum = 3  # 执行总数
        blackCount = 0  # 黑屏次数
        preWhiteIndex = 0  # 上一次白屏的下标
        name = '指挥中心合成图像1'
        print('测试源：' + name)

        # adbUtils.swipeDown(self.driver)
        # 无限循环
        # i = 1
        # while i > 0:

        for i in range(1, sum+1):

            self.driver.find_elements('xpath', "//*[@text='"+name+"']")[0].click()

            flag = True
            while flag:

                textele = self.driver.find_elements('id', 'imageClose')

                if len(textele) > 0:
                    # 图片对比
                    time.sleep(2)
                    isBlack = self.isSamePic(self.driver)
                    flag = False
                else:
                    time.sleep(1)

            if isBlack:
                time.sleep(3)
                isBlack = self.isSamePic(self.driver)
                if isBlack:
                    blackCount += 1
                    adbUtils.swipeDown(self.driver)
                    adbUtils.swipeDown(self.driver)
                    time.sleep(1)
                    self.driver.find_element_by_id('com.github.xiaofei_dev.vibrator:id/action').click()
                    time.sleep(2)
                    self.driver.find_element_by_id('com.github.xiaofei_dev.vibrator:id/action').click()
                    adbUtils.swipeUp(self.driver)
                    time.sleep(0.5)
                self.driver.find_element('id', 'imageClose').click()
                # 连续黑屏次数 = 当前执行数 - 上次白屏执行数
                black = i - preWhiteIndex
                if black == 5:
                    mailUtils.send_mail(black)
                    send_next_time = datetime.now() + timedelta(minutes=3)
                elif black > 5 and send_next_time < datetime.now():
                    mailUtils.send_mail(black, name)
                    send_next_time = datetime.now() + timedelta(minutes=3)

            else:
                self.driver.find_element('id', 'imageClose').click()
                preWhiteIndex = i

            # 计算出现黑屏的概率
            self.percentage(self.driver, sum, i, blackCount)

            time.sleep(1)
            i += 1

    def isSamePic(self, driver):

        imageAssert = ImageAssert(driver)

        # 截取当前整个屏幕,保存到本地
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")
        driver.get_screenshot_as_file(TEMP_FILE)
        file = open(TEMP_FILE, 'rb').read()
        allure.attach(file, 'screenshot_img', allure.attachment_type.PNG)

        # 把黑屏截图保存到本地，用做对比
        # river.get_screenshot_as_file("D:\\GZBAPP\\source\\black.png")
        load = imageAssert.load_image("D:\\GZBAPP\\source\\P20_Screenshot_20191228_105612_com.xfrhtx.gzb.jpg")

        # 要求误差500以内
        result = imageAssert.same_as(load, 200)
        return result

    # 计算出现黑屏的概率
    def percentage(self, driver, sum, i, blackCount):
        percentage = blackCount / i
        with allure.step(
                time.strftime('%Y-%m-%d %H:%M:%S') +
                ' 总执行数 ' + str(sum) +
                ' 执行次数 ' + str(i) +
                ' 黑屏次数 ' + str(blackCount) +
                ' 黑屏率为 ' + str(percentage)):
                    print(time.strftime('%Y-%m-%d %H:%M:%S'), ' 总执行数 ' + str(sum), '执行次数' + str(i),
                          '黑屏次数' + str(blackCount), '黑屏率为' + str(percentage))

    def teardown(self):
        self.driver.quit()
        print('finished')


# class DoTask:
#     def job(self):
#         pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
#         os.system('allure generate report/ -o report/html --clean')
#
#
# doTask = DoTask()
#
# if __name__ == '__main__':
#     time1 = "17:13:30"
#     time2 = "17:16"
#
#     # 第一轮
#     schedule.every().day.at(time1).do(doTask.job)
#
#     # 第二轮
#     schedule.every().day.at(time2).do(doTask.job)
#
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
