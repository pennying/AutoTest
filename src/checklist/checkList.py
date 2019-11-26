#!/usr/bin/env python
# coding:utf-8

from config.seleniumConfig import DriverClient

import time
import unittest
import warnings

from common import gobalvar
from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.chat import chatUtil
from common.utils.receiveMsgByhttp import sendMsgByHttpUtil
from common.utils.relay import relayUtil
from common.utils.recall import recallUtil
from common.utils.removeMsg import removeMsgUtil
from common.utils.copyMsg import copyMsgUtil
from common.utils.call import callUtil
from common.utils.group import groupUtil
from common.utils.confrence import confrenceUtil
from common.utils.report import reportUtil
from common.utils.chatAssert import chatAssert


class CheckTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    def test_00_login(self):
        openAppUtil.openapp(self.driver)
        loginUtil.login(self.driver)
        time.sleep(6)
        chatUtil.openChat(self.driver, gobalvar.chatTo)

    def test_01_sendText(self):
        flag = chatUtil.sendFlag(self.driver)
        messages = ['Hello! GZB.', u'沟通无远弗届']
        chatUtil.sendText(self.driver, messages[0])
        chatUtil.sendText(self.driver, messages[1])
        chatAssert.sendTextAssert(self.driver, flag, messages)

    def test_02_sendEmoji(self):
        flag = chatUtil.sendFlag(self.driver)
        messages = [[0, 1, 2, 3]]
        chatUtil.sendEmoji(self.driver, messages[0])
        chatAssert.sendEmojiAssert(self.driver, flag, messages)

    def test_03_sendLargeEmoji(self):
        flag = chatUtil.sendFlag(self.driver)
        messages = [0, 1]
        chatUtil.sendLargeEmoji(self.driver, messages)
        chatAssert.sendLargeEmojiAssert(self.driver, flag, messages)

    def test_04_sendImage(self):
        flag = chatUtil.sendFlag(self.driver)
        messages = [0]
        chatUtil.sendImage(self.driver, messages)
        chatAssert.sendImageAssert(self.driver, flag, messages)

    # def test_05_sendFile(self):
    #     chatUtil.sendFile(self.driver)
    #     print('发送文件成功')

    def test_05_sendVoice(self):
        chatUtil.sendVoice(self.driver)
        print('发送语音成功')

    def test_06_sendVideo(self):
        chatUtil.sendVideo(self.driver)
        print('发送小视频成功')

    def test_07_relayText(self):
        relayUtil.relayText(self.driver, '潘颖_测试', '潘颖_测试企业', ['潘颖', '汤彦祖'])
        print('转发文本成功')

    def test_08_relayFile(self):
        relayUtil.relayFile(self.driver, '潘颖_测试', '潘颖_测试企业', ['潘颖', '汤彦祖'])
        print('转发文件成功')

    def test_09_recall(self):
        recallUtil.recall(self.driver)
        print('撤回成功')

    def test_10_removeMsg(self):
        removeMsgUtil.removeMsg(self.driver)
        print('删除成功')

    def test_11_copyMsg(self):
        chatUtil.sendText(self.driver, 'Hello! copy this.')
        copyMsgUtil.copyMsg(self.driver)
        print('复制成功')

    def test_12_call(self):
        callUtil.call(self.driver)
        print('网络通话成功')

    def test_13_callPhone(self):
        callUtil.callPhone(self.driver, 13750061249)
        print('拨号盘呼叫外线成功')

    def test_14_newGroup(self):
        groupUtil.newGroup(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])
        print('创建群组成功！')

    def test_15_conf(self):
        confrenceUtil.confrence(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])

    # 接收文本
    def test_16_receiveMsg(self):
        sendMsgByHttpUtil.sendMsg('u307147', 'u1037134', 'test content')  # 文本
        sendMsgByHttpUtil.sendMsg('u307147', 'u1037134', '/花/大笑/可爱')  # 小表情

    # 接收大表情
    def test_17_receiveEmoji(self):
        sendMsgByHttpUtil.sendEmoji('u307147', 'u1037134', '牛')

    # 接收图片
    def test_18_receivePic(self):
        sendMsgByHttpUtil.sendPic('u307147', 'u1037134')

    # 接收文件
    def test_19_receiveFile(self):
        sendMsgByHttpUtil.sendFile('u307147', 'u1037134')

    # 接收语音
    def test_20_receiveVoice(self):
        sendMsgByHttpUtil.sendVoice('u307147', 'u1037134')

    def test_21_receiveshortvideo(self):
        sendMsgByHttpUtil.sendshortvideo('u307147', 'u1037134')

    def tearDown(self):
        print('test fished')


if __name__ == '__main__':
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(CheckTest)
    # suite = unittest.TestSuite([suite1])

    suite = unittest.TestSuite()
    suite.addTest(CheckTest('test_00_login'))
    suite.addTest(CheckTest('test_04_sendImage'))

    reportUtil.reportUtil('CheckListReport.html', '自动化冒烟测试结果', suite)
