import time
from appium import webdriver

# server 启动参数
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


# 1.6
# 0.7
# 0.9

print(time.time())
driver.swipe(100, 2000, 100, 1000, 3000)
print(time.time())

# swipe 通过 driver 使用的
# 传入 起始的位置x和y 和 结束的位置x和y
# 时间参数，越长滑动的约精准
# 默认的时间，自己测试 大约是 0.8（不准确）
# 如果获取当前的时间戳 time.time()
# 时间戳的含义是 从1970年到现在过了多少秒

# 拿到一个新的函数之后，先看官方的注释，碰到不认识的单词，去百度！
# 多实验，自己尝试总结结论。

