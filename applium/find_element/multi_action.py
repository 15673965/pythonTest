from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platforVersion']='7.1.2'

desired_caps['app']=r'H:\性能、自动化、接口02\App自动化appium+python\Appium python2018最新资料\appium教程相关软件\第四章软件\App\com.baidu.BaiduMap.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()

x=driver.get_window_size()['width']
y=driver.get_window_size()['height']

def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)


    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    print('start pinch...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

def zoom():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)


    action1.press(x=x*0.4,y=y*0.4).wait(1000).move_to(x=x*0.2,y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6,y=y*0.6).wait(1000).move_to(x=x*0.8,y=y*0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()
