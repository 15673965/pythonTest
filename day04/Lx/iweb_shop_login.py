# 导入unittest
import unittest
# 导入webdriver
from selenium import webdriver
from time import sleep
class TestLoginOut(unittest.TestCase):

    def setUp(self):
        # 实例化浏览器
        self.driver = webdriver.Firefox()
        # 打开浏览器
        url = 'http://192.168.13.20/iwebshop/'
        self.driver.get(url)
        # 最大化窗口
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(30)

        print("-------------")

    def test_iweb_login(self):
        print("x*20")
        # 获取driver
        driver = self.driver
        # 定位登录按钮跳转至登录页面
        driver.find_element_by_link_text("登录").click()
        # 定位用户名及操作
        aa = driver.find_element_by_css_selector("input[alt*='邮箱']")
        aa.send_keys("admin")
        # 定位面框及操作
        driver.find_element_by_css_selector("input[alt*='密码']").send_keys("123456")
        # 点击登录按钮
        driver.find_element_by_css_selector(".submit_login").click()
    def tearDown(self):
        # 点击退出
        sleep(2)
        self.driver.find_element_by_link_text("安全退出").click()
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
