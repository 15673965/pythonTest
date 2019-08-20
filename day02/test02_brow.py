from selenium import webdriver
from time import sleep
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册A.html")

sleep(2)
# 浏览器最大化
driver.maximize_window()
sleep(2)
# 设置浏览器宽、高(像素点)
driver.set_window_size(300,200)
sleep(2)
# 设置浏览器位置
driver.set_window_position(300,200)

sleep(3)

driver.quit()