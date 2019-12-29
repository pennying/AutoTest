class OpenAppUtil(object):

    def open_app(self, driver):

        driver.implicitly_wait(30)
        print('启动工作宝OK')

        # 设置权限
        driver.find_element('id', 'md_buttonDefaultPositive').click()
        driver.find_element('id', 'com.android.packageinstaller:id/permission_allow_button').click()
        print('权限设置OK')


openAppUtil = OpenAppUtil()
