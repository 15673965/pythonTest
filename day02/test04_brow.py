from selenium import webdriver
from time import sleep
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
sleep(2)

# 定位元素，打开新窗口
driver.find_element_by_link_text("注册A网页").click()
sleep(2)

# 关闭主窗口
driver.close()

sleep(3)
driver.quit()