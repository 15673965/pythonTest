import base64
from appium import webdriver
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
data = str(base64.b64encode('test 123'.encode('utf-8')), 'utf-8')
print(data)
driver.push_file('/sdcard/test.txt', data)

data = driver.pull_file('/sdcard/test.txt') # 返回数据为base64编码
print(str(base64.b64decode(data), 'utf-8')) # base64解码

