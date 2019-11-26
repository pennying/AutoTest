import time


class GroupUtil(object):

    def newGroup(self, driver, team, department, members):

        driver.find_element_by_id('com.jiahe.gzb:id/img_title_right_action').click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='新聊天'][1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='" + team + "'][1]").click()
        driver.find_element_by_xpath("//*[@text='" + department + "'][1]").click()
        for name in members:
            print(name)
            driver.find_element_by_xpath("//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btnOk').click()
        driver.find_element_by_id('com.jiahe.gzb:id/create_group').click()
        driver.find_element_by_id('com.jiahe.gzb:id/textLeftAction').click()


groupUtil = GroupUtil()
