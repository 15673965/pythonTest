from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException

import logging
import logging.config

stream=open('../yaml/desired_caps.yaml','r',encoding='UTF-8')
data=yaml.load(stream)

CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


desired_caps={}
desired_caps['platformName']=data['platformName']

desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['noReset']=data['noReset']

desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

def check_updateBtn():
    logging.info("check_pdateBtn")

    try:
        element = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('update element is not found!')
    else:
        element.click()


def check_skipBtn():
    logging.info("check_skipBtn")
    try:
        element = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('skipBtn element is not found!')
    else:
        element.click()

check_updateBtn()
check_skipBtn()
