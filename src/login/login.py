from config.config import DriverClient
from common.utils.openApp import openAppUtil

import warnings
import unittest
import time
from config import HTMLTestRunner
from common.utils.adbUtils import adbUtils


class LoginTest(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    # 验证用户登录
    def user_login(self, username, password):
        adbUtils.input(self.driver, 'com.jiahe.gzb:id/input_phone_num', username)
        adbUtils.input(self.driver, 'com.jiahe.gzb:id/input_password', password)
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()

    def test_login(self):
        print('open app')
        openAppUtil.openapp(self.driver)

    def test_login0(self):
        # 用户名、密码为空登录
        self.user_login('', '')
        print('用户名密码为空时，测试通过')

    def test_login1(self):
        # 用户名正确,密码为空
        self.user_login('13813807003', '')
        print('用户名正确、密码为空时，测试通过')

    def test_login2(self):
        # 用户名为空,密码正确
        self.user_login('', '123456')
        print('用户名为空、密码正确时，测试通过')

    def test_login3(self):
        # 用户名密码正确
        self.user_login('13813807002', '123456')
        print('用户名密码正确时，测试通过')

    def tearDown(self):
        print('test finished')


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite = unittest.TestSuite([suite1])

    # 设置测试报告保存路径
    file_path = '/Users/app/Documents/autoTest/TestReport/'
    # 获取系统当前时间
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 设置报告文件名称
    report_name = file_path + now + " LoginTestReport.html"

    fp = open(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告-登录', tester='PY', description='')
    runner.run(suite)
    fp.close()
