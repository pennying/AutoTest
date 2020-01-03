#!/usr/bin/env python
# coding:utf-8
import os
import time
import warnings
import tempfile
import allure
import pytest
import pytesseract
import cv2
from PIL import Image

from config.seleniumConfig import DriverClient
from common.utils.login_xf import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.imageAssert import ImageAssert


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

    def isSamePic(self, driver):

        imageAssert = ImageAssert(driver)

        # 截取当前整个屏幕,保存到本地
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")
        driver.get_screenshot_as_file(TEMP_FILE)

        # 把黑屏截图保存到本地，用做对比
        driver.get_screenshot_as_file("D:\\GZBAPP\\temp\\gray.png")
        load = imageAssert.load_image("D:\\GZBAPP\\temp\\gray.png")

        # 没有误差
        result = imageAssert.same_as(load, 0)
        return result

    def istatic(self, driver, pic_name):

        imageAssert = ImageAssert(driver)

        # 截取部分图片
        PATH = lambda p: os.path.abspath(p)
        TEMP_FILE = PATH(tempfile.gettempdir() + "/" + pic_name + ".png")
        imageAssert.get_screenshot_by_custom_size(1850, 75, 2050, 130)

        # 读入原始图像
        img = cv2.imread(TEMP_FILE)
        # 灰度化处理
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 放大图像
        fx = 4.0
        fy = 3.0
        img_new = cv2.resize(img_gray, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)

        # 保存图片
        img_new.save(TEMP_FILE)

        # # 写入图片到本地img_
        # save_folder = 'D:\\GZBAPP\\temp\\'
        # cv2.imwrite(os.path.join(save_folder, 'gray.jpg'), img_new)
        # FILE = save_folder + 'gray.jpg'
        #
        # cv2.namedWindow("roi")
        # cv2.imshow("roi", FILE)
        # cv2.waitKey(0)
        # cv2.destroyAllWindow()
        #
        # text = pytesseract.image_to_string(Image.open(FILE), config='--psm 7 sfz')
        #
        # print(text)
        #
        # if len(text) == 13:
        #     text = True
        # return text

    def teardown(self):
        print('finished')


if __name__ == '__main__':

    pytest.main(['-s', '-q', 'test_pushImage.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report -o /html --clean')
