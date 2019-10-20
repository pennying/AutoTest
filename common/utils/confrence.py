import time


class ConfrenceUtil(object):

    def confrence(self, driver, team, department, members):

        driver.find_element_by_id('com.jiahe.gzb:id/action_btn').click()
        time.sleep(1)
        # driver.find_element_by_xpath("//*[@text='召开会议'][2]").click()
        driver.find_elements_by_id('com.jiahe.gzb:id/menu_text')[1].click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='" + team + "'][1]").click()
        driver.find_element_by_xpath("//*[@text='" + department + "'][1]").click()
        for name in members:
            print(name)
            driver.find_element_by_xpath("//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_ok').click()
        # 首次安装才需要此权限，覆盖安装不需要
        tip = driver.find_elements_by_id('com.android.packageinstaller:id/permission_allow_button')
        if len(tip) > 0:
            driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        driver.find_element_by_id('com.jiahe.gzb:id/conf_begin_text').click()
        time.sleep(10)
        driver.find_element_by_id('com.jiahe.gzb:id/hangUp_btn').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/txt_backup')[2].click()
        time.sleep(2)


confrenceUtil = ConfrenceUtil()
