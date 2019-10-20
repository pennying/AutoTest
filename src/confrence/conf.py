#!/usr/bin/env python
# coding:utf-8

import warnings
import unittest
from config.seleniumConfig import DriverClient
from common.utils.openApp import openAppUtil
from common.utils.login import loginUtil
from common.utils.confrence import confrenceUtil


class ConfTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_0_conf(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)

    def test_1_conf(self):
        confrenceUtil.confrence(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    unittest.main()
