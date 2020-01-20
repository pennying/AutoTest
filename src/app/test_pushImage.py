#!/usr/bin/env python
# coding:utf-8
import os
import time
import warnings
import tempfile
import allure
import pytest
from datetime import datetime, timedelta

from config.seleniumConfig import DriverClient
from common.utils.login_xf import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.imageAssert import ImageAssert
from common.utils.adbUtils import adbUtils
from common.utils.mailUtil import mailUtils
from common.utils.mailwithzip import mailwithzip
from common.utils.listener import listener


@allure.feature("测试图像推送")
class TestTXTS:

    # 驱动
    def setup(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver(nosingleton=True)

    # 登录
    def login(self):
        openAppUtil.open_app(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    # 图像推送
    @allure.story('测试图像推送')
    def test_txts(self):

        """
        计算查看高清图像时出现黑屏的概率
        """
        self.login()
        self.driver.find_element('xpath', "//*[@text='图像推送']").click()
        time.sleep(3)
        self.driver.find_element('xpath', "//*[@text='内部测试（勿删）']").click()

        sum = 2  # 执行总数
        blackCount = 0  # 黑屏次数
        preWhiteIndex = 0  # 上一次白屏的下标
        name = '应急管理部指挥大厅主'
        print('测试源：' + name)

        # adbUtils.swipeDown(self.driver)
        # 无限循环
        # i = 1
        # while i > 0:
        # blackCountTimeList = []

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
                    # 黑屏的时间数组
                    # blackCountTimeList.append(time.strftime('%Y-%m-%d %H:%M:%S'))
                    # self.vibrator()
                self.driver.find_element('id', 'imageClose').click()
                # 连续黑屏次数 = 当前执行数 - 上次白屏执行数
                black = i - preWhiteIndex
                if black == 5:
                    # text = blackCountTimeList[0] + '到' + blackCountTimeList[-1] + '期间连续黑屏'
                    # print(text)
                    mailUtils.send_mail(black, name)
                    send_next_time = datetime.now() + timedelta(minutes=3)
                elif black > 5 and send_next_time < datetime.now():
                    # text = blackCountTimeList[0] + '到' + blackCountTimeList[-1] + '期间连续黑屏'
                    # print(text)
                    mailUtils.send_mail(black, name)
                    send_next_time = datetime.now() + timedelta(minutes=3)

            else:
                # blackCountTimeList = []
                self.driver.find_element('id', 'imageClose').click()
                preWhiteIndex = i

            # 计算出现黑屏的概率
            self.percentage(self.driver, sum, i, blackCount)

            # 写入log
            fileName = 'black_screen_log_' + time.strftime('%Y%m%d') + '.txt'
            filePath = 'D:\\GZBAPP\\src\\app\\log\\' + fileName

            with open(filePath, "a+", encoding="utf-8") as f:
                nintData = [
                    time.strftime('%Y-%m-%d %H:%M:%S'),
                    '  执行次数 ' + str(i),
                    '  黑屏次数 ' + str(blackCount),
                    '  黑屏率为 ' + str(blackCount / i),
                    '  连续黑屏 ' + str(i - preWhiteIndex) + "\n"
                ]
                f.writelines(nintData)
                f.close()

            self.writeTxt(isBlack)
            time.sleep(2)
            i += 1

    def send_mail(self, sum, blackCount):
        percentage = blackCount / sum
        mailText = time.strftime('%Y-%m-%d %H:%M:%S') + '\n总执行数 ' + str(sum) + '\n黑屏次数' + str(blackCount) + '\n黑屏率为' + str(percentage) + '\n黑屏时间 ' + str('见附件')
        FileName = 'black_screen_log_' + time.strftime('%Y%m%d') + '.txt'
        FilePath = 'D:\\GZBAPP\\src\\app\\log\\' + FileName
        mailwithzip.send_mail(FilePath, FileName, mailText)

    def isSamePic(self, driver):

        imageAssert = ImageAssert(driver)

        # 截取当前整个屏幕,保存到本地
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")

        hasGetScreen = driver.get_screenshot_as_file(TEMP_FILE)
        while not hasGetScreen:
            print('=========================截屏失败====================================')
            hasGetScreen = driver.get_screenshot_as_file(TEMP_FILE)

        file = open(TEMP_FILE, 'rb').read()
        allure.attach(file, 'screenshot_img', allure.attachment_type.PNG)

        # 把黑屏截图保存到本地，用做对比
        # river.get_screenshot_as_file("D:\\GZBAPP\\source\\black.png")
        load = imageAssert.load_image("D:\\GZBAPP\\source\\P10_Screenshot_20191207_230754_com.xfrhtx.gzb.jpg")

        # 要求完全一致
        result = imageAssert.same_as(load, 200)
        return result

    # 震动提醒
    def vibrator(self):
        adbUtils.swipeDown1(self.driver)
        adbUtils.swipeDown1(self.driver)
        time.sleep(1)
        self.driver.find_element_by_id('com.github.xiaofei_dev.vibrator:id/action').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.github.xiaofei_dev.vibrator:id/action').click()
        adbUtils.swipeUp(self.driver)
        time.sleep(0.5)

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

    def writeTxt(self, isBlack):

        # 测试报告路径
        curDate = time.strftime('%Y-%m-%d')
        fileName = "black_screen_report_" + curDate + '.txt'
        fileName = fileName.replace('-', '')
        filePath = 'D:\\GZBAPP\\src\\app\\log\\' + fileName

        sum = 0
        blackCount = 0

        # 如果文件不存在，则创建并初始化
        if not os.path.exists(filePath):

            f = open(filePath, "w+")
            nintData = [
                curDate + "\n",
                str(sum) + "\n",
                str(blackCount) + "\n"
            ]
            f.writelines(nintData)
            f.close()

        # 如果文件存在，则读取并更新数据
        if os.path.exists(filePath):
            f_read = open(filePath, mode='r+')
            lines = f_read.readlines()
            print(lines)
            sumCountInFile = int(lines[1].replace("\n", ""))
            blackCountInFile = int(lines[2].replace("\n", ""))
            sum = sumCountInFile + 1
            blackCount = blackCountInFile

        if isBlack:
            blackCount += 1

        newData = [
            curDate + "\n",
            str(sum) + "\n",
            str(blackCount) + "\n"
        ]
        f_write = open(filePath, 'w+')
        f_write.writelines(newData)
        f_read.close()

    def teardown(self):
        listener.listener('black_screen_report_')
        print('finished')


if __name__ == '__main__':
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')
