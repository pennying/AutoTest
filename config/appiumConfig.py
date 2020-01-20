from appium import webdriver


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'

            # 真机
            # desired_caps['platformVersion'] = '9'
            # desired_caps['deviceName'] = 'SJE0217317012319' # V10
            # desired_caps['deviceName'] = 'CLB7N18828002163' # P10

            # 模拟器
            desired_caps['plateformVersion'] = '6.0.1'
            desired_caps['deviceName'] = '127.0.0.1:4723'
            desired_caps['automationName'] = 'uiautomator2'

            # 7.0版本
            # desired_caps['appPackage'] = 'com.jiahe.gzb'
            # desired_caps['appActivity'] = 'com.jm.gzb.system.ui.activity.SplashActivity'
            # desired_caps['appWaitActivity'] = 'com.jm.gzb.system.ui.activity.SplashActivity'

            # 消防版
            desired_caps['appPackage'] = 'com.xfrhtx.gzb'
            desired_caps['appActivity'] = 'com.jm.gzb.system.ui.activity.SplashActivity'
            desired_caps['appWaitActivity'] = 'com.jm.gzb.system.ui.activity.SplashActivity'

            desired_caps['sessionOverride'] = True
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        return cls._instance


class AppiumDriverClient(Singleton):

    def getDriver(self):
        return self.driver
