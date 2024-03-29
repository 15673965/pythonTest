import time
from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

save_button = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more_button = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
battery_button = driver.find_element_by_xpath("//*[contains(@text,'电池')]")

# driver.scroll(save_button, more_button)
# driver.scroll(battery_button, save_button)

# 和 swipe相比 都存在一定的"惯性"
# 和 swipe相比 参数不同，一个是坐标（swipe），一个是元素（scroll）
