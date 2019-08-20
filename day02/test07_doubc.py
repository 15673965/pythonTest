from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")

# 定位元素
element = driver.find_element_by_css_selector("#user")

element.send_keys("admin")

sleep(2)
# 实例化ActionChains对象,在用户名文本框上双击鼠标左键，选中admin
ActionChains(driver).double_click(element).perform()

sleep(2)

driver.quit()