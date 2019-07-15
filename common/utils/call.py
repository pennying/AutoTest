import time


class CallUtil(object):
    def call(self, driver, username, calltype):
        print(username)
        print(calltype)
        driver.implicitly_wait(35)
        # driver.find_element_by_xpath("//*[@text='" + username + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/tab_call_imageview').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@text='" + calltype + "'][1]").click()
        # driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
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

        driver.find_elements_by_id('android:id/icon')[1].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[0].click()
        time.sleep(10)
        driver.find_element_by_id('com.jiahe.gzb:id/hangUp_btn').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[1].click()
        time.sleep(3)


callUtil = CallUtil()
