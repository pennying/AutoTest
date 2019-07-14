from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from common.utils.adbUtils import adbUtils


class OpenAppUtil(object):
    def openapp(self, driver):
        driver.implicitly_wait(30)
        print('启动工作宝OK')

        # 设置权限
        driver.find_element_by_id('com.jiahe.gzb:id/btn_positive').click()
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        print('权限设置OK')

        # 点击启动页
        # driver.find_element_by_class_name('android.widget.TextView').click()

        # 输入识别码
        WebDriverWait(driver, 20, 0.5, NoSuchElementException).until(
            lambda x: x.find_element_by_id('com.jiahe.gzb:id/corp_code_edit'))
        adbUtils.input(driver, 'com.jiahe.gzb:id/corp_code_edit', 'jmgzb')
        driver.find_element_by_id('com.jiahe.gzb:id/next_step_btn').click()
        driver.implicitly_wait(30)
        print('识别码OK')


openAppUtil = OpenAppUtil()
