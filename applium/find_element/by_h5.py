from  appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName']='Android'
# desired_caps['platformVersion']='7.1.2'
# desired_caps['deviceName']='127.0.0.1:62025'

# desired_caps['platformVersion'] = '8.1.0'
# desired_caps['deviceName'] = 'Honor 8X'
# desired_caps['udid'] = 'JQYRX18B28000934'

desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'MX4 Pro'
desired_caps['udid'] = '760BBL42328T'

desired_caps['app']=r'H:\性能、自动化、接口02\App自动化appium+python\Appium python2018最新资料\appium教程相关软件\第四章软件\H5元素定位软件全家桶\dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'
desired_caps["chromedriverExcutable"] = "C:\\Program Files\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\win\\chromedriver.exe"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

print('click BackupBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver,20).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('click NextBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver,20).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
contexts=driver.contexts
print(contexts)


#需android4.4及以上版本的系统中才会输出更多的webview
print('switch conetext')
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
print('edit email')
driver.find_element_by_id('email').send_keys('shuqing@wondershare.cn')
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()

#切换context 点击返回
driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()