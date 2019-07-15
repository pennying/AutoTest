from appium import webdriver

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '9'
            # desired_caps['deviceName'] = 'SJE0217317012319'
            desired_caps['automationName'] = 'uiautomator2'
            desired_caps['deviceName'] = 'SJE7N17706000615'
            desired_caps['appPackage'] = 'com.jiahe.gzb'
            desired_caps['appActivity'] = 'com.jiahe.gzb.ui.activity.SplashActivity'
            desired_caps['appWaitActivity'] = 'com.jiahe.gzb.ui.activity.SplashActivity'
            desired_caps['sessionOverride'] = True
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return cls._instance


class AppiumDriverClient(Singleton):

    def getDriver(self):
        return self.driver
