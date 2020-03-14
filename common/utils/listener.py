import pytest
import time
import os


class Listener:

    def listener(self, contentName, restartFile, max):
        os.system('start.bat')

        time.sleep(2)
        curDate = time.strftime('%Y-%m-%d')
        fileName = curDate + '.txt'
        fileName = fileName.replace('-', '')
        filePath = 'D:\\GZBAPP\\src\\app\\log\\' + contentName + fileName

        # 读文件
        f = open(filePath, "r+")
        lines = f.readlines()
        count = int(lines[1].replace("\n", ""))
        if count < max:
            pytest.main(['-s', restartFile, '--clean-alluredir', '--alluredir', 'report'])
        else:
            os.system('stop.bat')


listener = Listener()
