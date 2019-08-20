from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium import webdriver
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
driver.maximize_window()
sleep(2)
# 隐式等待 包含全局元素
driver.implicitly_wait(10)
driver.find_element_by_css_selector("#user").send_keys("admin")

driver.quit()

TouchAction
