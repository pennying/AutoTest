#!/usr/bin/env python
# coding:utf-8
import os
import time
import warnings
import tempfile
import allure
import pytest

from config.seleniumConfig import DriverClient
from common.utils.login_xf import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.imageAssert import ImageAssert
from common.utils.mailUtil import mailUtils


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
        self.login()
        self.driver.find_element('xpath', "//*[@text='图像推送']").click()
        time.sleep(3)
        self.driver.find_element('xpath', "//*[@text='佳米测试']").click()

        name = '指挥中心合成图像1'
        # name = '应急管理部指挥大厅主'

        self.driver.find_elements('xpath', "//*[@text='"+name+"']")[0].click()
        time.sleep(6)

        i = 0
        while i < 100:
            i += 1
            print(i)
            result = self.isSamePic(self.driver)
            time.sleep(1)

            if result:
                print('画面卡住了')
                mailUtils.send_mail_static(name)
            else:
                print('正常')

    def isSamePic(self, driver):

        imageAssert = ImageAssert(driver)

        self.sreenShoot(self.driver, 'pic1')
        time.sleep(1)
        self.sreenShoot(self.driver, 'pic2')

        result = imageAssert.same_as_1("pic1", "pic2", 0)

        return result

    def sreenShoot(self, driver, pic_name):

        imageAssert = ImageAssert(driver)

        # 截取当前整个屏幕,保存到本地
        # PATH = lambda p: os.path.abspath(p)
        # TEMP_FILE = PATH(tempfile.gettempdir() + "/" + pic_name + ".png")
        # driver.get_screenshot_as_file(TEMP_FILE)

        # 截取部分图片
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/" + pic_name + ".png")
        imageAssert.get_screenshot_by_custom_size(1850, 75, 2050, 130)
        driver.get_screenshot_as_file(TEMP_FILE)

    def teardown(self):
        print('finished')


if __name__ == '__main__':

    pytest.main(['-s', '-q', 'test_video.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')
