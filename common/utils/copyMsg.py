from common.utils.adbUtils import adbUtils
import unittest
import time


class CopyMsgUtil(unittest.TestCase):

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

    # 复制消息
    def copyMsg(self, driver):

        flag = True
        while flag:
            time.sleep(1)
            try:
                textele = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')

                if len(textele) > 0:
                    adbUtils.longpress(driver, 'com.jiahe.gzb:id/chat_msg_text', 3000)
                    driver.find_elements_by_id('com.jiahe.gzb:id/title')[2].click()
                    flag = False
                else:
                    self.swipeUp(driver)
            finally:
                print('滑动一次')


copyMsgUtil = CopyMsgUtil()
