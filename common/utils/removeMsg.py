from common.utils.adbUtils import adbUtils
import unittest


class RemoveMsgUtil(unittest.TestCase):

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

    # 删除消息
    def remove_msg(self, driver):

        self.swipeDown(driver)

        textele = driver.find_elements_by_id('com.jiahe.gzb:id/tv_content')[-1]
        adbUtils.longpress1(driver, textele, 3000)
        driver.find_elements_by_id('com.jiahe.gzb:id/md_title')[1].click()


removeMsgUtil = RemoveMsgUtil()
