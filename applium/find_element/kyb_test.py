from appium import webdriver
# import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
# desired_caps['platformVersion'] = '8.1.0'
# desired_caps['deviceName'] = 'Honor 8X'
# desired_caps['udid'] = 'JQYRX18B28000934'
# app信息
desired_caps['app'] = r'H:\性能、自动化、接口02\App自动化appium+python\Appium python2018最新资料\appium教程相关软件\第二章配套软件\App\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

# adb -P 5037 -s JQYRX18B28000934 install "kaoyan3.1.0.apk"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# time.sleep(2)

# driver.quit()