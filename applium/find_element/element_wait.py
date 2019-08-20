# from applium.find_element.kyb_login import driver
# from selenium.webdriver.support.ui import WebDriverWait
#
# WebDriverWait(driver, 10).until(lambda x : x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))
# driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  # 导入WebDriverWait类

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 超时时间为30s，每隔1秒搜索一次元素是否存在，如果元素存在返回定位对象并退出
search_button = WebDriverWait(driver, 30, 1).until(lambda x: x.find_element_by_id('com.android.settings:id/search'))
search_button.click()
driver.quit()
