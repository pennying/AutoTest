#!/usr/bin/env python 
# coding:utf-8
import time
import warnings
import unittest
from config.config import DriverClient
from common.utils.openApp import openAppUtil
from common.utils.login import loginUtil


class CallTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def call(self, username, calltype):
        print(username)
        print(calltype)
        time.sleep(35)
        self.driver.find_element_by_xpath("//*[@text='"+username+"'][1]").click()
        self.driver.find_element_by_id('com.jiahe.gzb:id/tab_call_imageview').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='"+calltype+"'][1]").click()
        time.sleep(10)
        self.driver.find_element_by_id('com.jiahe.gzb:id/hangup_btn').click()

    def test_call(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)

    def test_call0(self):
        self.call('乙1', '网络通话')

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    unittest.main()
