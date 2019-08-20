import yaml
import logging.config
from appium import webdriver


CON_LOG = '../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():

    stream = open('../yaml/desired_caps.yaml', 'r',encoding='UTF-8')
    data = yaml.load(stream)

    desired_caps={}
    desired_caps['platformName']=data['platformName']

    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    desired_caps['app']=data['app']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    logging.info('start run app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()
