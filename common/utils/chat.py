from common.utils.adbUtils import adbUtils
import unittest
import time
from common.utils.eleUtils import eleUtils


class ChatUtil(unittest.TestCase):

    # 打开会话窗
    def open_chat(self, driver, chatObj):
        driver.find_element_by_xpath("//*[@text='"+chatObj+"'][1]").click()

    # 发送标志位
    def send_flag(self, driver):
        flag = time.strftime('%Y-%m-%d %H:%M:%S')
        driver.find_element_by_id('com.jiahe.gzb:id/et_sendmessage').send_keys(flag)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()
        time.sleep(3)
        return flag

    # 文本
    def send_text(self, driver, message):
        # 发送文本
        driver.find_element_by_id('com.jiahe.gzb:id/et_sendmessage').send_keys(message)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()
        time.sleep(3)

    # 小表情
    def send_emoji(self, driver, emojiarr):

        # 发送小表情
        driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        ele = driver.find_elements_by_id('com.jiahe.gzb:id/iv_expression')
        for x in emojiarr:
            ele[x].click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()

    # 大表情
    def send_large_emoji(self, driver, largeEmojiarr):

        # 发送大表情
        driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        driver.implicitly_wait(10)
        driver.find_elements_by_id('com.jiahe.gzb:id/iv_icon')[2].click()
        ele = driver.find_elements_by_id('com.jiahe.gzb:id/iv_expression')
        for x in largeEmojiarr:
            ele[x].click()

    # 图片
    def send_image(self, driver, imagearr):

        # 发送图片相册
        driver.find_element_by_id('com.jiahe.gzb:id/btn_more').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[1].click()
        time.sleep(3)
        ele = driver.find_elements_by_id('com.jiahe.gzb:id/image')
        for x in imagearr:
            ele[x].click()

        driver.find_element_by_id('com.jiahe.gzb:id/textRightAction').click()

    # 图片
    def take_photo(self, driver):

        # 拍照发送图片
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[0].click()

        # 首次安装才需要此权限，覆盖安装不需要

        if eleUtils.isElementExistByID(driver, 'com.android.packageinstaller:id/permission_allow_button'):
            driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        driver.find_element_by_id('com.jiahe.gzb:id/switch_camera').click()
        driver.find_element_by_id('com.jiahe.gzb:id/startVideo').click()
        driver.find_element_by_id('com.jiahe.gzb:id/ok_img').click()
        driver.find_element_by_id('com.jiahe.gzb:id/original_btn').click()
        driver.find_element_by_id('com.jiahe.gzb:id/button_confirm').click()

    # 发送文件
    def send_file(self, driver):

        # 发送文件
        time.sleep(2)
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[2].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/linearLayout')[1].click()
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()

    # 发送语音
    def send_voice(self, driver):

        # 发送语音
        driver.find_element_by_id('com.jiahe.gzb:id/btn_set_mode_voice').click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_press_to_speak').click()
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        adbUtils.longpress(driver, 'com.jiahe.gzb:id/btn_press_to_speak', 3000)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_set_mode_keyboard').click()

    # 发送小视频
    def send_video(self, driver):

        # 发送小视频
        driver.find_element_by_id('com.jiahe.gzb:id/btn_more').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/image')[0].click()

        # 首次安装才需要此权限，覆盖安装不需要
        ele = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        if eleUtils.isElementExistByEle(ele):
            ele.click()

            adbUtils.longpress(driver, 'com.jiahe.gzb:id/startVideo', 1000)

        # 首次安装才需要此权限，覆盖安装不需要
        ele = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        if eleUtils.isElementExistByEle(ele):
            ele.click()

        driver.find_element_by_id('com.jiahe.gzb:id/switch_camera').click()
        adbUtils.longpress(driver, 'com.jiahe.gzb:id/startVideo', 6000)
        driver.find_element_by_id('com.jiahe.gzb:id/ok_img').click()
        time.sleep(3)


chatUtil = ChatUtil()
