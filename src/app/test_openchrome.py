# coding:utf-8

import time
from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 静默模式

driver = webdriver.Chrome()

# 打开chrome浏览器
driver = webdriver.Chrome(chrome_options=option)
# driver.get("http://rhtxav.119.gov.cn:8091/kdspzygl/#/login")

i = 0
while i < 30:

    openPage = 'window.open("http://rhtxav.119.gov.cn:8091/kdspzygl/#/login")'

    driver.execute_script(openPage)
    n = driver.window_handles  # 获取当前页句柄
    time.sleep(1)
    driver.switch_to.window(n[-1])  # 切换到新的网页窗口

    time.sleep(2)
    driver.find_elements_by_tag_name('input')[0].send_keys('jiami2')
    driver.find_elements_by_tag_name('input')[1].send_keys('123456')
    driver.find_element_by_id('keybtn').click()

    time.sleep(2)
    driver.find_elements_by_class_name('kc-menu-item')[0].click()
    time.sleep(2)
    driver.find_elements_by_class_name('kc-button--text')[0].click()
    i += 1
