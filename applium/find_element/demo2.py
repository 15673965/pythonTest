import time
from appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 获取更多按钮
more_button = driver.find_element_by_xpath("//*[contains(@text,'更多')]")

# 轻敲
# 只传入元素 就会点击元素
# TouchAction(driver).tap(more_button).perform()
# 只传入左边 会点击以屏幕左上角为原点 点击
# TouchAction(driver).tap(x=850, y=1500).perform()
# 元素和x和y都传，以元素为准
# TouchAction(driver).tap(more_button, 600, 600).perform()





# def hello(num1=None, num2=None, str1=None, str2=None):
#     print(num1)
#     print(num2)
#     print(str1)
#     print(str2)
#
#
#
# hello(str2=1, num2=2)
