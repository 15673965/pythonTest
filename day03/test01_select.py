# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
driver.maximize_window()
sleep(2)

# 定位select
webElement = driver.find_element_by_css_selector("select")

# 实例化select标签
select = Select(webElement)

# 1. 根据索引实现
select.select_by_index(1)
select.select_by_index(3)
select.select_by_index(2)
# 2. 根据文本值实现
select.select_by_visible_text("A上海")
select.select_by_visible_text("A重庆")
select.select_by_visible_text("A广州")
# 3. 根据value属性实现
select.select_by_value("sh")
select.select_by_value("cq")
select.select_by_value("gz")

driver.quit()

