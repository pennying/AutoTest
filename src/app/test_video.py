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
from common.utils.mailUtil import mailUtils
from common.utils.listener import listener


@allure.feature("测试图像推送")
class TestStatic:

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
        slowCount = 0

        self.login()
        self.driver.find_element('xpath', "//*[@text='图像推送']").click()
        time.sleep(3)
        self.driver.find_element('xpath', "//*[@text='内部测试（勿删）']").click()

        name = '指挥中心合成图像1'
        # name = '应急管理部指挥大厅主'

        self.driver.find_elements('xpath', "//*[@text='"+name+"']")[0].click()
        time.sleep(6)
        slowCountTimeList = []
        i = 0
        while i < 2:
            i += 1
            isSlow = self.isSamePic(self.driver)
            time.sleep(1)

            if isSlow:
                # 卡顿次数
                slowCount += 1
                print(time.strftime('%Y-%m-%d %H:%M:%S'), '执行次数' + str(i), '画面卡住了')
                # 卡顿的时间数组
                # slowCountTimeList.append(time.strftime('%Y-%m-%d %H:%M:%S'))
                # 发送邮件次数
                sendCount = 0
                if sendCount < 3:
                    if slowCount == 5 or (slowCount > 5 and send_next_time < datetime.now()):
                        # text = slowCountTimeList[0] + '到' + slowCountTimeList[-1] + '期间连续卡顿'
                        mailUtils.send_mail_static(name, slowCount)
                        send_next_time = datetime.now() + timedelta(minutes=3)
                        sendCount += 1
            else:
                # slowCountTimeList = []
                print(time.strftime('%Y-%m-%d %H:%M:%S'), '执行次数' + str(i), '正常')

            self.writeTxt(isSlow)

            # 写入log
            fileName = 'kadun_log_' + time.strftime('%Y%m%d') + '.txt'
            filePath = 'D:\\GZBAPP\\src\\app\\log\\' + fileName

            with open(filePath, "a+", encoding="utf-8") as f:
                nintData = [
                    time.strftime('%Y-%m-%d %H:%M:%S'),
                    '  执行次数 ' + str(i),
                    '  卡顿次数 ' + str(slowCount) + "\n"
                ]
                f.writelines(nintData)
                f.close()

    def isSamePic(self, driver):

        imageAssert = ImageAssert(driver)

        self.sreenShoot(self.driver, 'pic1')
        time.sleep(1)
        self.sreenShoot(self.driver, 'pic2')

        result = imageAssert.same_as_1("pic1", "pic2", 0)

        return result

    def sreenShoot(self, driver, pic_name):

        # 截取当前整个屏幕,保存到本地
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/" + pic_name + ".png")
        driver.get_screenshot_as_file(TEMP_FILE)

        # 截取部分图片
        # imageAssert = ImageAssert(driver)
        # PATH = lambda p: os.path.abspath(p)
        # TEMP_FILE = PATH(tempfile.gettempdir() + "/" + pic_name + ".png")
        # imageAssert.get_screenshot_by_custom_size(1850, 75, 2050, 130)
        # driver.get_screenshot_as_file(TEMP_FILE)

    def writeTxt(self, isSlow):

        # 测试报告路径
        curDate = time.strftime('%Y-%m-%d')
        fileName = 'kadun_report_' + curDate + '.txt'
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

        if isSlow:
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
        listener.listener('kadun_report_')
        print('finished')


if __name__ == '__main__':
    os.system('start.bat')
    pytest.main(['-s', '-q', 'test_video.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')
