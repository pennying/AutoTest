#!/usr/bin/env python 
#coding:utf-8
import time
from selenium import webdriver
from time import sleep
import unittest


class talkTest(unittest.TestCase):

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
        time.sleep(3)
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

        time.sleep(5)
        #跳过版本更新
        self.driver.find_element_by_id('com.jiahe.gzb:id/buttonDefaultNegative').click()
        #等待响应时间
        time.sleep(5)
        #客服小宝
        self.driver.find_element_by_xpath("//*[@text='客服小宝'][1]").click()

    def sendText(self, message):        
        #发送文本
        self.driver.find_element_by_id('com.jiahe.gzb:id/et_sendmessage').send_keys(message)
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()

    def test_1_sendText(self):
        #发送英文
        self.sendText('Hello!I have something that want to ask for you.')
        #发送中文
        self.sendText(u'您好！我有一些问题想要向您咨询')
        #发送特殊字符
        self.sendText(u'！@＃¥％……&＊（）——＋')
        #发送链接
        self.sendText('www.baidu.com')
 
    def sendEmoji(self, emojiArr):
        #发送表情
        self.driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        ele = self.driver.find_elements_by_xpath('//android.widget.ImageView[@resource-id="com.jiahe.gzb:id/iv_expression"]')
        for x in emojiArr:
            ele[x].click()
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_send').click()

        #发送表情
        #driver.find_element_by_id('com.jiahe.gzb:id/rl_face').click()
        #ele = driver.find_elements_by_xpath('//android.widget.ImageView[@resource-id="com.jiahe.gzb:id/iv_expression"]')
        #ele[1].click()
        #ele[2].click()
        #ele[3].click()
        #driver.find_element_by_id('com.jiahe.gzb:id/iv_expression')[.click()
        
    def test_2_sendEmoji(self):
        self.sendEmoji([1, 3, 5, 7])


    def tearDown(self):
    	print('test fished')
    	self.driver.quit()


if __name__ == '__main__':
    unittest.main()