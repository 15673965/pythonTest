import time
from appium import webdriver


class TestSetting:

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62025'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # def test_mobile_network_2g(self):
    #     self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
    #     self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
    #     self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
    #     self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobile_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    # def test_mobile_display_input(self):
    #     self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
    #     self.driver.find_element_by_id("com.android.settings:id/search").click()
    #     self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
    #     self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    def teardown(self):
        self.driver.quit()
