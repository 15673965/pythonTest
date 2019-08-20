from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")

# 定位元素
element = driver.find_element_by_css_selector("#user")
# 实例化ActionChains对象,在用户名文本框上点击鼠标右键
ActionChains(driver).context_click(element).perform()

sleep(3)

driver.quit()