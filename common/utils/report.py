import time
from config import HTMLTestRunner
import unittest


class ReportUtil(object):

    def reportUtil(self, filename, title, suite):

        # 设置测试报告保存路径
        file_path = '/Users/app/Documents/autoTest/TestReport/'

        # 获取系统当前时间
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())

        # 设置报告文件名称
        report_name = file_path + now + filename

        fp = open(report_name, 'wb')
        unittest.TextTestRunner(verbosity=2)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=''+title+'', tester='PY', description='')
        runner.run(suite)
        fp.close()


reportUtil = ReportUtil()
