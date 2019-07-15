from common.utils.adbUtils import adbUtils
import unittest
import time


class RelayUtil(unittest.TestCase):

    # 获取屏幕大小
    def getSize(self, driver):
        # 获得屏幕大小宽和高
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return [x, y]

    # 屏幕向下\上滑动
    def swipeUp(self, driver):
        # 手指向上滑动
        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        adbUtils.swipe(driver, x1, y2, x1, y1)

    # 转发文本
    def relay(self, driver):
        flag = True
        while flag:
            time.sleep(2)
            try:
                textele = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')

                if len(textele) > 0:
                    adbUtils.longpress(driver, 'com.jiahe.gzb:id/chat_msg_text', 3000)
                    flag = False
                else:
                    self.swipeUp(driver)
            except:
                print('未找到元素')

        driver.find_elements_by_id('com.jiahe.gzb:id/title')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/name')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/name_layout')[0].click()
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()


relayUtil = RelayUtil()
