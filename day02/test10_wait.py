from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")

driver.maximize_window()
element = (By.CSS_SELECTOR, "#user")
WebDriverWait(driver, 10).until(EC.presence_of_element_located(element)).send_keys("admin")
driver.quit()
