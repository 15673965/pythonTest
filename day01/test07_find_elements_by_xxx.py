# 导入selenium
from selenium import webdriver
# 导入time包
from time import sleep
# 实例化火狐浏览器
driver=webdriver.Firefox()
# 打开注册A.html
url='F:\\BaiduYunDownload\\webdriverspace\\sources\\注册A.html'
driver.get(url)
'''
查找定位所有符合条件的元素，返回的定位元素格式为数组(列表)格式
'''
driver.find_elements_by_tag_name("input")[1].send_keys("123456")
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
