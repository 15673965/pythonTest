# 导入selenium
from selenium import webdriver
# 导入time包
from time import sleep
# 实例化火狐浏览器
driver=webdriver.Firefox()
# 打开注册A.html
url='F:\\BaiduYunDownload\\webdriverspace\\sources\\注册A.html'
driver.get(url)
# 通过class_name定位元素及操作
driver.find_element_by_class_name("telA").send_keys("18111265465")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
