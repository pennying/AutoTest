import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.utils.adbUtils import adbUtils
from common import gobalvar


class LoginUtil(object):
    def login(self, driver):

        # 输入识别码
        WebDriverWait(driver, 20, 0.5, NoSuchElementException).until(
            lambda x: x.find_element_by_id('com.jiahe.gzb:id/corp_code_edit'))
        adbUtils.input(driver, 'com.jiahe.gzb:id/corp_code_edit', gobalvar.service)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_next').click()
        driver.implicitly_wait(30)
        print('识别码OK')

        # 登录
        adbUtils.input(driver, 'com.jiahe.gzb:id/edit_account', gobalvar.account)
        adbUtils.input(driver, 'com.jiahe.gzb:id/edit_password', gobalvar.password)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()
        time.sleep(2)
        print('登录OK')

        # 一键保活
        driver.find_element_by_id('com.jiahe.gzb:id/btn_title_close').click()
        print('跳过一键保活OK')


loginUtil = LoginUtil()
