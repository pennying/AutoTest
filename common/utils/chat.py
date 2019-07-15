from common.utils.adbUtils import adbUtils
import unittest
import time


class ChatUtil(unittest.TestCase):

    # 文本
    def sendText(self, driver, username, message):

        # 发送文本
        driver.find_element_by_id('com.jiahe.gzb:id/et_sendmessage').send_keys(message)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()
        time.sleep(3)

        # 验证文本
        textarry = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')
        lasttext = textarry[-1]
        self.assertEqual(lasttext.text, message, ' 未发送')
        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')

    # 小表情
    def sendEmoji(self, driver, emojiarr):

        # 发送小表情
        driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        ele = driver.find_elements_by_xpath(
            '//android.widget.ImageView[@resource-id="com.jiahe.gzb:id/iv_expression"]')
        for x in emojiarr:
            ele[x].click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()

        # 验证小表情
        emojitextlist = ["/棒", "/鼓掌", "/握手", "/耶", "/花", "/调皮", "/飞吻", "/喜欢", "/媚眼", "/奋斗", "/眨眼",
                         "/捂嘴", "/可爱", "/大笑", "/微笑", "/呲牙", "/抠鼻", "/难过", "/害羞", "/衰", ]

        time.sleep(2)
        textarry = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')
        emojitext = ''
        for x in emojiarr:
            emojitext += emojitextlist[x]

        lasttext = textarry[-1]

        self.assertEqual(lasttext.text, emojitext, ' 表情不对应')

        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')

    # 大表情
    def sendLargeEmoji(self, driver, largeEmojiarr):

        # 发送大表情
        driver.find_elements_by_id('com.jiahe.gzb:id/iv_icon')[1].click()
        ele = driver.find_elements_by_id('com.jiahe.gzb:id/iv_expression')
        for x in largeEmojiarr:
            ele[x].click()

        # 验证大表情
        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')

    # 图片
    def sendImage(self, driver, imagearr):

        # 发送图片
        driver.find_element_by_id('com.jiahe.gzb:id/btn_more').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[1].click()
        ele = driver.find_elements_by_id('com.jiahe.gzb:id/image')
        for x in imagearr:
            ele[x].click()
        driver.find_element_by_id('com.jiahe.gzb:id/commit').click()

        # 验证图片
        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')

    # 发送文件
    def sendFile(self, driver):

        # 发送文件
        time.sleep(2)
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[2].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[1].click()
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()

        # 验证文件
        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')

    # 语音
    def sendVoice(self, driver):

        # 发送语音
        driver.find_element_by_id('com.jiahe.gzb:id/btn_set_mode_voice').click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_press_to_speak').click()
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        adbUtils.longpress(driver, 'com.jiahe.gzb:id/btn_press_to_speak', 3000)

        # 验证语音
        readarry = driver.find_elements_by_id('com.jiahe.gzb:id/tv_unread')
        lastread = readarry[-1]
        self.assertEqual(lastread.text, '未读', '发送失败')


chatUtil = ChatUtil()
