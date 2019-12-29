#!/usr/bin/env python
# coding:utf-8
import os
import time
import warnings
import pytest

from config.seleniumConfig import DriverClient
from common.utils.login import loginUtil
from common.utils.openApp import openAppUtil
from common.utils.openTab import openTabUtil
from common.utils.chat import chatUtil
from common.utils.relay import relayUtil
from common.utils.recall import recallUtil
from common.utils.removeMsg import removeMsgUtil
from common.utils.copyMsg import copyMsgUtil
from common.utils.receiveMsgByhttp import sendMsgByHttpUtil
from common.utils.chatAssert import chatAssert
from common.utils.group import groupUtil


class TestChat:

    # 驱动
    def setup(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    # 登录
    def test_login(self):
        openAppUtil.open_app(self.driver)
        loginUtil.login(self.driver)
        time.sleep(8)
        openTabUtil.open_tab(self.driver)
        time.sleep(8)

    def test_create_group(self):
        groupUtil.create_group(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])

    # 发送文本
    def test_send_text(self):
        flag = chatUtil.send_flag(self.driver)
        messages = ['Hello! GZB.', u'沟通无远弗届']
        chatUtil.send_text(self.driver, messages)
        chatAssert.send_text_assert(self.driver, flag, messages)

    # 发送emoji表情
    def test_send_emoji(self):
        flag = chatUtil.send_flag(self.driver)
        messages = [[0, 1, 2, 3]]
        chatUtil.send_emoji(self.driver, messages[0])
        chatAssert.sendEmojiAssert(self.driver, flag, messages)

    # 发送大表情
    def test_send_large_emoji(self):
        flag = chatUtil.send_flag(self.driver)
        messages = [0, 1]
        chatUtil.send_large_emoji(self.driver, messages)
        chatAssert.sendLargeEmojiAssert(self.driver, flag, messages)

    # 发送图片
    def test_send_image(self):
        flag = chatUtil.send_flag(self.driver)
        messages = [0]
        chatUtil.send_image(self.driver, messages)
        chatAssert.sendImageAssert(self.driver, flag, messages)

    # 拍照发送图片
    def test_take_photo(self):
        chatUtil.take_photo(self.driver)

    # 发送文件
    def test_send_file(self):
        chatUtil.send_file(self.driver)

    # 发送语音
    def test_send_voice(self):
        chatUtil.send_voice(self.driver)

    # 发送小视频
    def test_send_video(self):
        chatUtil.send_video(self.driver)

    # 转发文本
    def test_relay_text(self):
        chatUtil.send_flag(self.driver)
        relayUtil.relay_text(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])
        print('转发文本成功')

    # 转发文件
    def test_relay_file(self):
        relayUtil.relay_file(self.driver, '潘颖_测试', '潘颖_部门1', ['颖1', '颖2'])
        print('转发文件成功')

    # 消息撤回
    def test_recall(self):
        chatUtil.send_flag(self.driver)
        recallUtil.recall(self.driver)

    # 消息删除
    def test_remove(self):
        chatUtil.send_flag(self.driver)
        removeMsgUtil.remove_msg(self.driver)

    # 消息复制
    def test_copy(self):
        chatUtil.send_flag(self.driver)
        copyMsgUtil.copy_msg(self.driver)

    # 接收文本
    def test_receive_msg(self):
        sendMsgByHttpUtil.send_msg('u307147', 'u1037134', 'test content')  # 文本
        sendMsgByHttpUtil.send_msg('u307147', 'u1037134', '/花/大笑/可爱')  # 小表情

    # 接收大表情
    def test_receive_emoji(self):
        sendMsgByHttpUtil.send_emoji('u307147', 'u1037134', '牛')

    # 接收图片
    def test_receive_pic(self):
        sendMsgByHttpUtil.send_pic('u307147', 'u1037134')

    # 接收文件
    def test_receive_file(self):
        sendMsgByHttpUtil.send_file('u307147', 'u1037134')

    # 接收语音
    def test_receive_voice(self):
        sendMsgByHttpUtil.send_voice('u307147', 'u1037134')

    # 接收小视频
    def test_receive_video(self):
        sendMsgByHttpUtil.send_short_video('u307147', 'u1037134')

    @staticmethod
    def teardown():
        print('finished')


if __name__ == '__main__':

    pytest.main(['-s', '-q', 'test_chatinGroup.py', '--clean-alluredir', '--alluredir', 'report'])
    os.system('allure generate report/ -o report/html --clean')
