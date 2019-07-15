from common.utils.adbUtils import adbUtils
import unittest
import time
from common import gobalvar


class RecallUtil(unittest.TestCase):

    # 获取屏幕大小
    def getSize(self, driver):
        # 获得屏幕大小宽和高
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return [x, y]

    # 屏幕向上滑动
    def swipeUp(self, driver):
        # 手指向上滑动
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        adbUtils.swipe(driver, x1, y1, x1, y2)

    # 屏幕向下滑动
    def swipeDown(self, driver):
        # 手指向上滑动
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        adbUtils.swipe(driver, x1, y1, x1, y2)

    # 撤回文本
    def recall(self, driver):
        time.sleep(5)

        self.swipeDown(driver)

        textele = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')
        textele = textele[-1]
        adbUtils.longpress1(driver, textele, 3000)

        driver.find_elements_by_id('com.jiahe.gzb:id/title')[3].click()

        # 验证撤回
        sysmsgarry = driver.find_elements_by_id('com.jiahe.gzb:id/chat_sysmsg_text')
        sysmsg = sysmsgarry[-1]
        self.assertEqual(sysmsg.text, gobalvar.username+'已撤回一条消息', '撤回失败')
        print('撤回成功')

    # 撤回文本
    def recallfail(self, driver):
        time.sleep(5)

        i = 0
        while i <= 7:
            i += 1
            self.swipeUp(driver)

        textele = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')

        if len(textele) > 0:
            textele = textele[-1]
            adbUtils.longpress1(driver, textele, 3000)

        driver.find_elements_by_id('com.jiahe.gzb:id/title')[3].click()

        # 验证撤回
        tip = driver.find_element_by_id('com.jiahe.gzb:id/content')
        self.assertEqual(tip.text, '撤回失败，发送时间超过 2 分钟的消息，不能被撤回。', '未弹出撤回失败的弹窗')
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()
        time.sleep(3)


recallUtil = RecallUtil()
