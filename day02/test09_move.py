from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")

driver.maximize_window()
sleep(2)

# 将模拟鼠标悬停 用户注册A 按钮，显示加入会员A提示
ActionChains(driver).move_to_element(driver.find_element_by_css_selector("#zc>fieldset>button")).perform()

sleep(2)

driver.quit()