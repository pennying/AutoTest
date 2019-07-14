import time
from common.utils.adbUtils import adbUtils


class LoginUtil(object):
    def login(self, driver):

        # 登录
        adbUtils.input(driver, 'com.jiahe.gzb:id/input_phone_num', '13813807030')
        adbUtils.input(driver, 'com.jiahe.gzb:id/input_password', '123456')
        driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()
        time.sleep(2)
        print('登录OK')

        # 一键保活
        driver.find_element_by_id('com.jiahe.gzb:id/btn_title_close').click()
        print('跳过一键保活OK')


loginUtil = LoginUtil()
