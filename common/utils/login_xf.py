import time
from common.utils.adbUtils import adbUtils
from common import gobalvar


class LoginUtil(object):
    def login(self, driver):

        # 隐私权限
        # time.sleep(2)
        # driver.find_element('id', 'btn_agree').click()

        # 登录
        adbUtils.input(driver, 'edit_account', gobalvar.account_xf)
        adbUtils.input(driver, 'edit_password', gobalvar.password_xf)
        driver.find_element('id', 'btn_login').click()
        time.sleep(2)
        print('登录OK')

        # 一键保活
        driver.find_element('id', 'btn_title_close').click()
        print('跳过一键保活OK')

        # 跳过更新
        driver.find_element('id', 'md_buttonDefaultNegative').click()
        print('跳过更新OK')


loginUtil = LoginUtil()
