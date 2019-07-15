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


openAppUtil = OpenAppUtil()
