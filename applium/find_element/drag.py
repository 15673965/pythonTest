import time
from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

save_button = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more_button = driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# battery_button = driver.find_element_by_xpath("//*[contains(@text,'电池')]")


# driver.drag_and_drop(save_button, more_button)
# driver.drag_and_drop(save_button, more_button)
# driver.drag_and_drop(save_button, more_button)
driver.drag_and_drop(save_button, more_button)


# user_button = driver.find_element_by_xpath("//*[contains(@text,'用户')]")
#
# driver.drag_and_drop(user_button, save_button)

# scroll 和 drag 的 区别  drag没有"惯性"
# 相同点：都是使用元素进行传参
# 和swipe项目， 一个传的是元素（drag），一个传的是坐标（swipe），
# 当swipe的时间足够长的时候，和drag的效果相同

# find_ele 如果找到了某个元素 会将具体位置缓存在系统中，
# 只要不重新获取，就算已经跑出屏幕外，也会认为元素在之前缓存的位置

# 只要某个元素在屏幕中出现了一部分，find_ele也会正常找到

