#!/usr/bin/env python
# coding:utf-8

from config.config import DriverClient

import time
import unittest
import warnings

from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.chat import chatUtil
from common.utils.relay import relayUtil
from common.utils.recall import recallUtil
from config import HTMLTestRunner


class ChatTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_0_sendText(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    def test_1_sendText(self):
        # 发送英文
        chatUtil.sendText(self.driver, '颖1', 'Hello!I have something that want to ask for you.')

        # 发送中文
        chatUtil.sendText(self.driver, '颖1', u'您好！我有一些问题想要向您咨询')

        # 发送特殊字符
        chatUtil.sendText(self.driver, '潘颖1', u'！@＃¥％……&＊（）——＋')

        # 发送链接
        chatUtil.sendText(self.driver, '潘颖1', 'www.baidu.com')

    def test_2_sendEmoji(self):
        chatUtil.sendEmoji(self.driver, [1, 3, 5, 7])

    def test_3_sendLargeEmoji(self):
        chatUtil.sendLargeEmoji(self.driver, [0, 1, 2, 3])

    def test_4_sendImage(self):
        chatUtil.sendImage(self.driver, [6, 7, 8])

    def test_5_sendFile(self):
        chatUtil.sendFile(self.driver)

    def test_6_sendVoice(self):
        chatUtil.sendVoice(self.driver)

    def test_7_relay(self):
        relayUtil.relay(self.driver)

    def test_8_recall(self):
        recallUtil.recall(self.driver)

    def test_9_recallfail(self):
        recallUtil.recallfail(self.driver)

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ChatTest)
    suite = unittest.TestSuite([suite1])

    # 设置测试报告保存路径
    file_path = '/Users/app/Documents/autoTest/TestReport/'
    # 获取系统当前时间
    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 设置报告文件名称
    report_name = file_path + now + " ChatTestReport.html"

    fp = open(report_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告-消息', tester='PY', description='')
    runner.run(suite)
    fp.close()
