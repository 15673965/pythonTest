from appium import webdriver
import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.1.2'
# desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platformVersion'] = '9.0.1'
desired_caps['deviceName'] = 'Honor 8X'
desired_caps['udid'] = 'JQYRX18B28000934'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# time.sleep(2)

# driver.quit()