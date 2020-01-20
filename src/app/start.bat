@echo on

title startAppiumServer

taskkill /f /t /im node.exe

cd /d C:\Users\work\AppData\Local\Programs\Appium\resources\app\node_modules\appium\build\lib

start /b node main.js -a 127.0.0.1 -p 4723 --relaxed-security --session-override --default-capabilities "{\"platformName\":\"Android\",\"deviceName\":\"SJE0217317012319\",\"app\":\"D:\\gzb\\XFRHTX_Android_V7.1.70_debug.apk\"}"
