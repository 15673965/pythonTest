from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")

driver.maximize_window()
sleep(2)
# 模拟键盘操作
# 用户名填admin1
driver.find_element_by_css_selector("#user").send_keys("admin1")
sleep(2)
# 删除一个字符
driver.find_element_by_css_selector("#user").send_keys(Keys.BACK_SPACE)
sleep(2)
# 全选
driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL, "a")
sleep(2)
# 复制
driver.find_element_by_css_selector("#user").send_keys(Keys.CONTROL, "c")
sleep(2)
# 粘贴
driver.find_element_by_css_selector("#password").send_keys(Keys.CONTROL, "v")
sleep(2)
driver.quit()