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
from common.utils.call import callUtil
from common.utils.group import groupUtil
from common.utils.report import reportUtil


class ChatTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_00_login(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)

    def test_01_sendText(self):
        self.driver.find_element_by_xpath("//*[@text='颖1'][1]").click()

        # 发送英文
        chatUtil.sendText(self.driver, '颖1', 'Hello!I have something that want to ask for you.')

        # 发送中文
        chatUtil.sendText(self.driver, '颖1', u'您好！我有一些问题想要向您咨询')

        # 发送特殊字符
        chatUtil.sendText(self.driver, '颖1', u'！@＃¥％……&＊（）——＋')

        # 发送链接
        chatUtil.sendText(self.driver, '颖1', 'www.baidu.com')

        print('发送消息成功')

    def test_02_sendEmoji(self):
        chatUtil.sendEmoji(self.driver, [1, 3, 5, 7])
        print('发送小表情成功')

    def test_03_sendLargeEmoji(self):
        chatUtil.sendLargeEmoji(self.driver, [0, 1, 2, 3])
        print('发送大表情成功')

    def test_04_sendImage(self):
        chatUtil.sendImage(self.driver, [6, 7, 8])
        print('发送图片成功')

    def test_05_sendFile(self):
        chatUtil.sendFile(self.driver)
        print('发送文件成功')

    def test_06_sendVoice(self):
        chatUtil.sendVoice(self.driver)
        print('发送语音成功')

    def test_07_relay(self):
        relayUtil.relay(self.driver)
        print('转发成功')

    def test_08_recall(self):
        recallUtil.recall(self.driver)
        print('撤回成功')

    def test_09_call(self):
        callUtil.call(self.driver, '颖1', '网络通话')
        print('网络通话成功')

    def test_10_callPhone(self):
        callUtil.callPhone(self.driver, 13631230850)
        print('拨号盘呼叫外线成功')

    def test_11_newGroup(self):
        groupUtil.newGroup(self.driver, '潘颖_测试企业2', '潘颖_部门1', ['颖1', '颖2'])
        print('创建群组成功！！')

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ChatTest)
    suite = unittest.TestSuite([suite1])

    reportUtil.reportUtil('CheckListReport.html', suite)
