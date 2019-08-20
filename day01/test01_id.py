# 导入selenium
from selenium import webdriver
# 导入time包
from time import sleep

# 实例化火狐浏览器
driver = webdriver.Firefox()
# 打开注册A.html
url = 'F:\\BaiduYunDownload\\webdriverspace\\sources\\注册A.html'
driver.get(url)
# 调用id定位方法
user = driver.find_element_by_id("userA")
# 使用send_keys()方法发送数据
user.send_keys("admin")
# 调用id定位方法
pwd = driver.find_element_by_id("passwordA")
# 使用send_keys()方法发送数据
pwd.send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
