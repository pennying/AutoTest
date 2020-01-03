# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions()
# option.add_argument('headless')  # 静默模式

# 打开chrome浏览器
sum = 3
for i in range(1, sum+1):
    driver = webdriver.Chrome( chrome_options=option)
    driver.get("https://www.cnblogs.com/yoyoketang")
    print(driver.title)
