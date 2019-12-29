#!/usr/bin/env python
# coding:utf-8

from config.seleniumConfig import DriverClient

import os
import time
import warnings
import pytest

from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.group import groupUtil


class TestGroup:

    def setup(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_login(self):
        openAppUtil.open_app(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    def test_create_group(self):
        groupUtil.create_group(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])
        print('创建群组成功！')

    def test_add_member(self):
        groupUtil.add_member(self.driver, '潘颖_测试', '潘颖_部门1', ['颖3', '颖5'])

    def test_remove_member(self):
        groupUtil.remove_member(self.driver)

    def test_alter_name(self):
        groupUtil.alter_name(self.driver)

    def test_dimensional_barcode(self):
        groupUtil.dimensional_barcode(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])

    def test_disbanded_group(self):
        groupUtil.disbanded_group(self.driver)

    def teardown(self):
        print('finished')


if __name__ == '__main__':

    pytest.main(['-s', '-q', 'test_group.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report/ -o report/html --clean')
