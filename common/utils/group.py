import time

from common.utils.selectedMem import selectedMenUtil
from common.utils.adbUtils import adbUtils



class GroupUtil(object):

    def create_group(self, driver, team, department, members):

        driver.find_element_by_id('com.jiahe.gzb:id/img_title_right_action').click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='发起群聊']").click()
        time.sleep(1)
        selectedMenUtil.selected_member(driver, team, department, members)
        driver.find_element_by_id('com.jiahe.gzb:id/create_group').click()
        time.sleep(1)

    def add_member(self, driver, team, department, members):
        driver.find_element_by_id('com.jiahe.gzb:id/iv_action_setting').click()
        driver.find_elements_by_id('com.jiahe.gzb:id/imgAvatar')[-2].click()
        selectedMenUtil.selected_member(driver, team, department, members)
        time.sleep(1)

    def remove_member(self, driver):
        driver.find_elements_by_id('com.jiahe.gzb:id/imgAvatar')[-1].click()
        driver.find_elements_by_id('com.jiahe.gzb:id/imgAvatar')[-3].click()
        driver.find_element_by_id('com.jiahe.gzb:id/btn_positive').click()
        time.sleep(1)

    def alter_name(self, driver):
        driver.find_element_by_id('com.jiahe.gzb:id/session_name').click()
        driver.find_element_by_id('com.jiahe.gzb:id/et_content').clear()
        driver.find_element_by_id('com.jiahe.gzb:id/et_content').send_keys('测试群组：修改名称')
        driver.find_element_by_id('com.jiahe.gzb:id/textRightAction').click()
        time.sleep(1)

    def dimensional_barcode(self, driver, team, department, members):
        driver.find_element_by_id('com.jiahe.gzb:id/textRightAction').click()
        driver.find_element_by_xpath("//*[@text='分享二维码']").click()
        selectedMenUtil.selected_member(driver, team, department, members)
        driver.find_element_by_id('com.jiahe.gzb:id/tv_app_name').click()

    def disbanded_group(self, driver):

        flag = True
        while flag:
            time.sleep(1)
            try:
                textele = driver.find_elements_by_id('com.jiahe.gzb:id/exit_or_dissolve')

                if len(textele) > 0:
                    driver.find_element_by_id('com.jiahe.gzb:id/exit_or_dissolve').click()
                    driver.find_element_by_id('com.jiahe.gzb:id/md_buttonDefaultPositive').click()
                    flag = False
                else:
                    adbUtils.swipeDown(driver)
            finally:
                print('未找到元素')


groupUtil = GroupUtil()
