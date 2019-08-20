'''
import pytest
class TestLogin:
    @pytest.mark.run(order=2)
    def test_login2(self):
        print("2")

    @pytest.mark.run(order=1)
    def test_login1(self):
        print("1")
        assert False

    @pytest.mark.run(order=1.5)
    def test_login15(self):
        print("1.5")

    @pytest.mark.skip(True, reason="done")
    def test_login3(self):
        print("3")

    @pytest.mark.run(order=0)
    def test_login0(self):
        print("0")

    @pytest.mark.run(order=-1)
    def test_login_1(self):
        print("-1")

    @pytest.mark.run(order=-2)
    def test_login_2(self):
        print("-2")

    def test_login(self):
        print("无标记")
'''
from appium import webdriver

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
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
