from selenium import webdriver
from time import sleep
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册A.html")

# 实现需求
sleep(2)
driver.find_element_by_css_selector("#userA").send_keys("admin")
sleep(2)
driver.find_element_by_css_selector("#passwordA").send_keys("admin")
sleep(2)
driver.find_element_by_css_selector("#telA").send_keys("1345678900")
sleep(2)
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
sleep(2)
# 修改电话号码
driver.find_element_by_css_selector("#telA").clear()
driver.find_element_by_css_selector("#telA").send_keys("18111111111")

sleep(3)

driver.quit()