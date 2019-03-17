import time


class LoginUtil(object):
    def login(self, driver):
        driver.find_element_by_id(
            'com.jiahe.gzb:id/input_phone_num').send_keys(13813807002)
        driver.find_element_by_id(
            'com.jiahe.gzb:id/input_password').send_keys(123456)
        driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()
        time.sleep(3)
        driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultNegative').click()


loginUtil = LoginUtil()
