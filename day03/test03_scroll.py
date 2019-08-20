# 导包
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
driver.maximize_window()
sleep(2)

# 定义js脚本
'''
   0:左边距；1000：上边距；单位像素
'''
js1="window.scrollTo(0,1000)"
sleep(2)
# 执行js语句
driver.execute_script(js1)
sleep(2)

# 2秒后回到初始位置
js2 = "window.scrollTo(0,0)"
driver.execute_script(js2)
sleep(2)
driver.quit()

