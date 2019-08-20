import time
from appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.ChooseLockPattern'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 执行手势
# TouchAction(driver)\
#     .press(x=231, y=842)\
#     .move_to(x=480, y=0)\
#     .move_to(x=480, y=0)\
#     .move_to(x=0, y=480)\
#     .move_to(x=-480, y=480)\
#     .move_to(x=-480, y=-480)\
#     .release()\
#     .perform()


# 执行手势
(TouchAction(driver)
 .press(x=231, y=842)
 .move_to(x=480, y=0)
 .move_to(x=480, y=0)
 .move_to(x=0, y=480)
 .move_to(x=-480, y=480)
 .move_to(x=-480, y=-480)
 .release()
 .perform())

# tap 轻巧
# press 按下
# long_press 长按
# wait 等待
# release 松手
# move_to 移动
# perform 执行

# 知道什么是链条？
# 一堆动作 通过  动作.动作.动作.动作.perform 这一串动作就是链条

# 关于代码过长的问题
# 两种方式 （用哪种都可以）
# - 直接在.之前回车，此时上一行末尾会有一个 "\"。"\"表示后面还有内容，并且是一行的
# - 在前后加 "（）"，再进行回车

