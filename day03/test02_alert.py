# 导包
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
sleep(2)

# 点击alert按钮
driver.find_element_by_css_selector("#alert").click()

# 1.获取警告框
alert = driver.switch_to.alert
# 处理对话框
text = alert.text
print("文本框内容： ", text)
# 同意
alert.accept()
# 取消
# alert.dismiss()

# 输入注册信息
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("#password").send_keys("123456")
driver.find_element_by_css_selector("#tel").send_keys("18111265465")
driver.find_element_by_css_selector("#email").send_keys("1188@qq.com")

driver.quit()

