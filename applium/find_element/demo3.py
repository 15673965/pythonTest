# -*- coding: utf-8 -*-
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
# 中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 声明对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 手机时间
print(driver.device_time)
# 获取当前手机的分辨率
print(driver.get_window_size())
# 宽
print(driver.get_window_size()["width"])
print(type(driver.get_window_size()["width"]))