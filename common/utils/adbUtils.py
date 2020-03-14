class AdbUtils(object):
    def input(self, driver, elementid, msg):
        driver.implicitly_wait(20)
        driver.find_element_by_id(elementid).click()
        driver.execute_script('mobile:shell', {'command': 'input text', 'args': msg})

    def longpress(self, driver, elementid, ms):
        driver.implicitly_wait(20)
        el = driver.find_element_by_id(elementid)
        elx = el.location.get('x')
        ely = el.location.get('y')
        args = str(elx) + ' ' + str(ely) + ' ' + str(elx) + ' ' + str(ely) + ' ' + str(ms)
        driver.execute_script('mobile:shell', {'command': 'input touchscreen swipe', 'args': args})

    def longpress1(self, driver, element, ms):
        el = element
        elx = el.location.get('x')
        ely = el.location.get('y')
        args = str(elx) + ' ' + str(ely) + ' ' + str(elx) + ' ' + str(ely) + ' ' + str(ms)
        driver.execute_script('mobile:shell', {'command': 'input touchscreen swipe', 'args': args})

    def swipe(self, driver, x1, y1, x2, y2, ms=100):
        args = str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2) + ' ' + str(ms)
        driver.execute_script('mobile:shell', {'command': 'input touchscreen swipe', 'args': args})

    # 获取屏幕大小
    def getSize(self, driver):

        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return [x, y]

    # 屏幕向上滑动
    def swipeUp(self, driver):

        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.swipe(driver, x1, y1, x1, y2)

    # 屏幕向下滑动
    def swipeDown(self, driver):

        l = self.getSize(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.00)  # 终点y坐标
        adbUtils.swipe(driver, x1, y1, x1, y2)

    # 屏幕向下滑动
    def swipeDown1(self, driver):

        l = self.getSize(driver)
        y1 = int(l[0] * 0.5)  # x坐标
        x1 = int(l[1] * 0.00)  # 起始y坐标
        x2 = int(l[1] * 0.75)  # 终点y坐标
        adbUtils.swipe(driver, x1, y1, x2, y1)


adbUtils = AdbUtils()
