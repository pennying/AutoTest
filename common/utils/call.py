import time


class CallUtil(object):
    def call(self, driver, username, callType):
        print(username)
        print(callType)
        driver.implicitly_wait(35)
        driver.find_element_by_id('com.jiahe.gzb:id/tab_call_imageview').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@text='" + callType + "'][1]").click()
        time.sleep(10)
        driver.find_element_by_id('com.jiahe.gzb:id/hangUp_btn').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[1].click()
        driver.find_element_by_id('android:id/icon').click()

    def callPhone(self, driver, phonenumber):
        time.sleep(1)
        driver.find_elements_by_id('android:id/icon')[1].click()
        #  设置通讯录权限
        driver.find_element_by_id('com.jiahe.gzb:id/btn_positive').click()
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        phonenumber = str(phonenumber)
        phonenumber = list(phonenumber)
        for x in phonenumber:
            id = 'com.jiahe.gzb:id/button' + str(x)
            driver.find_element_by_id(id).click()

        driver.find_elements_by_id('android:id/icon')[2].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[0].click()
        # 首次安装才需要此权限，覆盖安装不需要
        tip = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        if len(tip) > 0:
            driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(10)
        driver.find_element_by_id('com.jiahe.gzb:id/hangUp_btn').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[1].click()
        time.sleep(3)


callUtil = CallUtil()
