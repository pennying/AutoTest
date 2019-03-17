#coding:utf-8
import time
from selenium import webdriver
from time import sleep
import unittest

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '4.4.2'
            desired_caps['unicodeKeyboard'] = 'Ture'
            desired_caps['resetKeyboard'] = 'Ture'
            desired_caps['deviceName'] = '127.0.0.1:62001'

            # desired_caps['platformVersion'] = '5.0.1 Lollipop(API Level 21)'
            # #desired_caps['automationName'] = 'selenium'
            # desired_caps['deviceName'] = '292dd4aa'
            # desired_caps['noReset'] = True
            # #desired_caps['app'] = 'GZB_Android_V4.5.01_37512.apk'
            # #desired_caps['appPackage'] = 'com.dianxin.os.service'
            # # desired_caps['appActivity'] = 'MainActivity'
            # desired_caps['noSign'] = "True";

            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._instance

class DriverClient(Singleton):

    def getDriver(self):
        return self.driver