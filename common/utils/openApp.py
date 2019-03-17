import time


class OpenAppUtil(object):
    def openapp(self, driver):
        time.sleep(3)
        print('－－－－－－－－－工作宝启动成功－－－－－－－－－－')
        # 点击启动页
        driver.find_element_by_class_name('android.widget.TextView').click()
        print('启动页加载正常')
        time.sleep(3)
        # 验证识别码
        driver.find_element_by_id(
            'com.jiahe.gzb:id/corp_code_edit').send_keys('jmgzb')
        driver.find_element_by_id(
            'com.jiahe.gzb:id/next_step_btn').click()
        time.sleep(3)
        print('识别码正确')


openAppUtil = OpenAppUtil()
