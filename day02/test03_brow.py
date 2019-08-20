from selenium import webdriver
from time import sleep
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册A.html")

# 浏览器最大化
driver.maximize_window()
sleep(2)

# 跳转到新页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
sleep(2)

# 后退
driver.back()
sleep(2)

# 前进
driver.forward()
sleep(2)

# 刷新
driver.refresh()

sleep(3)
driver.quit()