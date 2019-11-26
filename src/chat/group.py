#!/usr/bin/env python
# coding:utf-8

from config.seleniumConfig import DriverClient

import time
import warnings
import unittest

from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.group import groupUtil


class group(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_00_login(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    def test_01_newGroup(self):
        groupUtil.newGroup(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])
        print('创建群组成功！')

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    unittest.main()
