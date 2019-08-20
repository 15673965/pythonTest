# 导入selenium
from selenium import webdriver
# 导入time包
from time import sleep
# 实例化火狐浏览器
driver=webdriver.Firefox()
# 打开注册A.html
url='F:\\BaiduYunDownload\\webdriverspace\\sources\\注册A.html'
driver.get(url)
# 定位账号及操作
driver.find_element_by_name("userA").send_keys("admin")
# 定位密码及操作
driver.find_element_by_name("passwordA").send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
