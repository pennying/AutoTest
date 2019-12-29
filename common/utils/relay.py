from common.utils.adbUtils import adbUtils
import unittest
import time


class RelayUtil(unittest.TestCase):

    # 转发文本
    def relay_text(self, driver, team, department, members):

        flag = True
        while flag:
            time.sleep(1)
            try:
                textele = driver.find_elements_by_id('com.jiahe.gzb:id/tv_content')

                if len(textele) > 0:
                    adbUtils.longpress(driver, 'com.jiahe.gzb:id/tv_content', 3000)
                    flag = False
                else:
                    adbUtils.swipeUp(driver)
            finally:
                print('未找到元素')

        driver.find_elements_by_id('com.jiahe.gzb:id/md_title')[0].click()
        driver.find_element_by_xpath("//*[@text='" + team + "'][1]").click()
        driver.find_element_by_xpath("//*[@text='" + department + "'][1]").click()
        for name in members:
            driver.find_element_by_xpath("//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btnOk').click()
        driver.find_element_by_id('com.jiahe.gzb:id/md_buttonDefaultPositive').click()

    # 转发文件
    def relay_file(self, driver, team, department, members):
        flag = True
        while flag:
            time.sleep(2)
            try:
                fileele = driver.find_elements_by_id('com.jiahe.gzb:id/file_name')

                if len(fileele) > 0:
                    adbUtils.longpress(driver, 'com.jiahe.gzb:id/file_name', 3000)
                    flag = False
                else:
                    self.swipeUp(driver)
            finally:
                print('未找到元素')

        driver.find_elements_by_id('com.jiahe.gzb:id/md_title')[0].click()
        driver.find_element_by_xpath("//*[@text='" + team + "'][1]").click()
        driver.find_element_by_xpath("//*[@text='" + department + "'][1]").click()
        for name in members:
            driver.find_element_by_xpath("//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btnOk').click()
        driver.find_element_by_id('com.jiahe.gzb:id/md_buttonDefaultPositive').click()


relayUtil = RelayUtil()
