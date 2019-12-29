import time
import unittest
from common.utils.eleUtils import eleUtils


class CallUtil(unittest.TestCase):

    def call(self, driver):
        driver.implicitly_wait(35)
        driver.find_element_by_id('com.jiahe.gzb:id/iv_action_call').click()

        ele = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        if eleUtils.isElementExist(ele):
            ele.click()

        time.sleep(20)
        driver.find_elements_by_id('com.jiahe.gzb:id/img_btn')[6].click()
        time.sleep(3)
        driver.find_element_by_id('com.jiahe.gzb:id/textLeftAction').click()

    def callPhone(self, driver, phonenumber):
        time.sleep(1)
        driver.find_element_by_id('com.jiahe.gzb:id/img_title_right_action').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/menu_text')[1].click()

        #  设置通讯录权限
        # driver.find_element_by_id('com.jiahe.gzb:id/btn_positive').click()
        # driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        phonenumber = str(phonenumber)
        phonenumber = list(phonenumber)
        for x in phonenumber:
            id = 'com.jiahe.gzb:id/button' + str(x)
            driver.find_element_by_id(id).click()

        driver.find_element_by_id('com.jiahe.gzb:id/ib_make_call').click()

        # 首次安装才需要此权限，覆盖安装不需要
        # tip = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        # if len(tip) > 0:
        #     driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        time.sleep(6)
        driver.find_elements_by_id('com.jiahe.gzb:id/img_btn')[6].click()
        driver.find_element_by_id('com.jiahe.gzb:id/ib_close').click()
        time.sleep(3)


callUtil = CallUtil()
