from appium import webdriver
import time

desired_caps={}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'

desired_caps['app'] = r'H:\性能、自动化、接口02\App自动化appium+python\Appium python2018最新资料\appium教程相关软件\第二章配套软件\App\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

time.sleep(2)
driver.find_element_by_id("android:id/button2").click()
time.sleep(2)
driver.find_element_by_id("com.tal.kaoyan:id/tv_skip").click()

time.sleep(2)

driver.quit()