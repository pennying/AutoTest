from common.utils.adbUtils import adbUtils
import unittest


class RemoveMsgUtil(unittest.TestCase):

    # 删除消息
    def remove_msg(self, driver):

        adbUtils.swipeUp(driver)

        textele = driver.find_elements_by_id('com.jiahe.gzb:id/tv_content')[-1]
        adbUtils.longpress1(driver, textele, 3000)
        driver.find_elements_by_id('com.jiahe.gzb:id/md_title')[1].click()


removeMsgUtil = RemoveMsgUtil()
