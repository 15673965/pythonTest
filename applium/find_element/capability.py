
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


desired_caps={}
# 平台信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['automationName']='uiautomator2' # 方便识别Toast元素
# app信息
desired_caps['app'] = r'H:\性能、自动化、接口02\App自动化appium+python\Appium python2018最新资料\appium教程相关软件\第二章配套软件\App\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
# 是否不重置session 默True
desired_caps['noReset'] = False
# unicode编码，允许中文输入
desired_caps['unicodeKeyboard'] = True
# 是否重置键盘输入
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 隐式等待
driver.implicitly_wait(3)

def check_cancle():
    try:
        cancle = driver.find_element_by_id("android:id/button2")
        cancle.click()
    except NoSuchElementException:
        print('no cancle button')

def check_skip():
    try:
        skip = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
        skip.click()
    except NoSuchElementException:
        print('no skip button')

if __name__ == '__main__':
    check_cancle()
    check_skip()