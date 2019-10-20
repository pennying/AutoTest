from common.utils.adbUtils import adbUtils
import unittest


class MultiSelectedUtil(unittest.TestCase):

    # 多选消息
    def multiSelectedMsg(self, driver, selectedNum):

        textele = driver.find_elements_by_id('com.jiahe.gzb:id/chat_msg_text')[-1]
        adbUtils.longpress1(driver, textele, 3000)
        driver.find_elements_by_id('com.jiahe.gzb:id/title')[4].click()
        textarry = driver.find_elements_by_id('com.jiahe.gzb:id/multi_selected')
        for x in selectedNum:
            textarry[x].click()

    # 多选转发
    def multiRelay(self, driver, selectedNum):

        multiSelectedUtil.multiSelectedMsg(driver, selectedNum)

        # 多选转发
        driver.find_element_by_id('com.jiahe.gzb:id/zhuan_fa').click()
        driver.find_element_by_id('com.jiahe.gzb:id/txt_backup').click()

        driver.find_elements_by_id('com.jiahe.gzb:id/name')[0].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/name_layout')[0].click()
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()
        driver.find_element_by_id('android:id/icon').click()

    # 多选保存
    def multiSave(self, driver, selectedNum):

        multiSelectedUtil.multiSelectedMsg(driver, selectedNum)

        # 多选保存
        driver.find_element_by_id('com.jiahe.gzb:id/bao_chun').click()
        tip = driver.find_elements_by_id('com.jiahe.gzb:id/buttonDefaultPositive')
        if len(tip) > 0:
            driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultPositive').click()
        driver.find_element_by_id('android:id/icon').click()

    # 多选删除
    def multiDel(self, driver, selectedNum):

        multiSelectedUtil.multiSelectedMsg(driver, selectedNum)

        # 多选删除
        driver.find_element_by_id('com.jiahe.gzb:id/shan_chu').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')


multiSelectedUtil = MultiSelectedUtil()
