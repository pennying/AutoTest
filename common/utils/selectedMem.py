class SelectedMenUtil(object):

    def selected_member(self, driver, team, department, members):
        driver.find_element('xpath', "//*[@text='" + team + "'][1]").click()
        driver.find_element('xpath', "//*[@text='" + department + "'][1]").click()
        for name in members:
            driver.find_element('xpath', "//*[@text='" + name + "'][1]").click()
        driver.find_element_by_id('com.jiahe.gzb:id/btnOk').click()


selectedMenUtil = SelectedMenUtil()
