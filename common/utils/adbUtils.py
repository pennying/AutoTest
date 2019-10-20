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


adbUtils = AdbUtils()
