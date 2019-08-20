from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\drop.html")

sleep(2)
# 源元素
source = driver.find_element_by_css_selector("#div1")
# 目标元素
target = driver.find_element_by_css_selector("#div2")

# 模拟鼠标拖动动作，选定拖动源元素释放到目标元素
ActionChains(driver).drag_and_drop(source, target).perform()

sleep(2)

driver.quit()