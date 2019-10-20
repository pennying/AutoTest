import time


class GroupUtil(object):

    def newGroup(self, driver, team, department, members):

        driver.find_element_by_id('com.jiahe.gzb:id/action_btn').click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='新建群聊'][1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='" + team + "'][1]").click()
        driver.find_element_by_xpath("//*[@text='" + department + "'][1]").click()
        for name in members:
            print(name)
            driver.find_element_by_xpath("//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_ok').click()
        driver.find_element_by_id('android:id/icon').click()


groupUtil = GroupUtil()
