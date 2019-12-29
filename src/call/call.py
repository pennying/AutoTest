#!/usr/bin/env python 
# coding:utf-8

import warnings
import unittest
import time
from config.seleniumConfig import DriverClient
from common.utils.openApp import openAppUtil
from common.utils.login import loginUtil
from common.utils.chat import chatUtil
from common.utils.call import callUtil


class CallTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_0_call(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(2)
        chatUtil.openChat(self.driver, '潘颖1')

    def test_1_call(self):
        callUtil.call(self.driver)

    def test_2_callPhone(self):
        callUtil.callPhone(self.driver, 13750061249)

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    unittest.main()
