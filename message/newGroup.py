#!/usr/bin/env python 
#coding:utf-8
import time
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.support.wait import WebdriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class newGroup(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1 Lollipop(API Level 21)'
		#设置支持中文编码
        desired_caps['unicodeKeyboard'] = 'Ture'
        desired_caps['resetKeyboard'] = 'Ture'
        #desired_caps['automationName'] = 'selenium'
        desired_caps['deviceName'] = '4d00501bf2fb407f'
        #desired_caps['app'] = 'GZB_Android_V4.5.01_37512.apk'
        #desired_caps['appPackage'] = 'com.dianxin.os.service'
        #desired_caps['appActivity'] = 'MainActivity'

        #启动app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    	#等待响应时间
        WebdriverWait(self.driver, 10).util(EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.Button')))
        #time.sleep(3)
        print('－－－－－－－－－工作宝启动成功－－－－－－－－－－')
            
    	#点击启动页
    	self.driver.find_element_by_class_name('android.widget.TextView').click()
    	print('启动页加载正常')

    	#验证识别码
        self.driver.find_element_by_id('com.jiahe.gzb:id/corp_code_edit').send_keys('jmgzb')
        self.driver.find_element_by_id('com.jiahe.gzb:id/next_step_btn').click()
        print('识别码正确')

        #验证用户登录
        self.driver.find_element_by_id('com.jiahe.gzb:id/input_phone_num').send_keys('13750061249')
        self.driver.find_element_by_id('com.jiahe.gzb:id/input_password').send_keys('123456')
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()
        print('登录成功！')
 
        WebdriverWait(self.driver, 5).util(EC.presence_of_element_located((By.ID, 'com.jiahe.gzb:id/buttonDefaultNegative')))
        #time.sleep(5)
        #跳过版本更新
        self.driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultNegative').click()
        #等待响应时间
        time.sleep(15)

    def newGroup(self, team, department, members):
    	self.driver.find_element_by_id('com.jiahe.gzb:id/action_btn').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='新建群聊'][1]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@text='"+team+"'][1]").click()
        self.driver.find_element_by_xpath("//*[@text='"+department+"'][1]").click()
        for name in members:
            print(name)
            self.driver.find_element_by_xpath("//*[@text='"+name+"'][1]").click()
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_ok').click()

    def test_1_newGroup(self):
        self.newGroup('呀 颖宝呐', '部门1', ['甲1', '乙1'])
        print('创建群组成功！')

    def tearDown(self):
    	print('test fished')
    	self.driver.quit()


if __name__ == '__main__':
    unittest.main()