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
传入要定位的元素，部分文本但需要唯一性
'''
driver.find_element_by_partial_link_text("访问").click()
# 暂停3秒
sleep(3)
# 关闭浏览器
driver.quit()
