#!/usr/bin/env python
# coding:utf-8

from config.seleniumConfig import DriverClient

import time
import unittest
import warnings

from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.chat import chatUtil
from common.utils.relay import relayUtil
from common.utils.recall import recallUtil
from common.utils.report import reportUtil
from common.utils.removeMsg import removeMsgUtil
from common.utils.copyMsg import copyMsgUtil
from common.utils.multiSelected import multiSelectedUtil
from common.utils.receiveMsgByhttp import sendMsgByHttpUtil


class ChatTest(unittest.TestCase):

    # 驱动
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    # 登录
    def test_00_login(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(5)
        chatUtil.openChat(self.driver, '颖1')

    # 发送文本
    def test_01_sendText(self):
        # 发送英文
        chatUtil.sendText(self.driver, 'Hello!This is a message for test.')

        # 发送中文
        chatUtil.sendText(self.driver, u'您好！这是条测试信息！')

        # 发送特殊字符
        chatUtil.sendText(self.driver, u'！@＃¥％……&＊（）——＋')

        # 发送链接
        chatUtil.sendText(self.driver, 'www.baidu.com')

    # 发送emoji表情
    def test_02_sendEmoji(self):
        chatUtil.sendEmoji(self.driver, [1, 3, 5, 7])

    # 发送大表情
    def test_03_sendLargeEmoji(self):
        chatUtil.sendLargeEmoji(self.driver, [0, 1, 2, 3])

    # 发送图片
    def test_04_sendImage(self):
        chatUtil.sendImage(self.driver, [6, 7, 8])

    # 发送文件
    def test_05_sendFile(self):
        chatUtil.sendFile(self.driver)

    # 发送语音
    def test_06_sendVoice(self):
        chatUtil.sendVoice(self.driver)

    # 发送小视频
    def test_07_sendVideo(self):
        chatUtil.sendVideo(self.driver)

    # 转发文本
    def test_08_relayText(self):
        relayUtil.relayText(self.driver)

    # 转发文件
    def test_09_relayFile(self):
        relayUtil.relayFile(self.driver)

    # 消息撤回
    def test_10_recall(self):
        recallUtil.recall(self.driver)

    # 消息删除
    def test_11_removeMsg(self):
        removeMsgUtil.removeMsg(self.driver)

    # 消息复制
    def test_12_copyMsg(self):
        copyMsgUtil.copyMsg(self.driver)

    # 消息多选
    def test_13_multiselected(self):
        multiSelectedUtil.multiRelay(self.driver, [1, 2, 3])
        multiSelectedUtil.multiSave(self.driver, [1, 2, 3])
        multiSelectedUtil.multiDel(self.driver, [1, 2, 3])

    # 接收文本
    def test_14_ReceiveMsg(self):
        sendMsgByHttpUtil.sendMsg(self.driver, 'u307147', 'u1037134', 'test content')  # 文本
        sendMsgByHttpUtil.sendMsg(self.driver, 'u307147', 'u1037134', '/花/大笑/可爱')  # 小表情

    # 接收大表情
    def test_15_ReceiveEmoji(self):
        sendMsgByHttpUtil.sendEmoji('u307147', 'u1037134', '牛')

    # 接收图片
    def test_16_ReceivePic(self):
        sendMsgByHttpUtil.sendPic(self.driver, 'u307147', 'u1037134')

    # 接收文件
    def test_17_ReceiveFile(self):
        sendMsgByHttpUtil.sendFile(self.driver, 'u307147', 'u1037134')

    # 接收语音
    def test_18_ReceiveVoice(self):
        sendMsgByHttpUtil.sendVoice(self.driver, 'u307147', 'u1037134')

    def test_19_Receiveshortvideo(self):
        sendMsgByHttpUtil.sendshortvideo('u307147', 'u1037134')

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(ChatTest)
    suite = unittest.TestSuite([suite1])

    # suite = unittest.TestSuite()
    # suite.addTest(ChatTest('test_00_login'))
    # suite.addTest(ChatTest('test_19_sendshortvideo'))

reportUtil.reportUtil('CheckListReport.html', '自动化测试报告-消息', suite)
