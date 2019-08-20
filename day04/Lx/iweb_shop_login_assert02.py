# 导入unittest
import sys
import time
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
    # 逆向登录
    def test_iweb_login(self):
        print("x*20")
        # 获取driver
        driver = self.driver
        # 定位登录按钮跳转至登录页面
        driver.find_element_by_link_text("登录").click()
        # 定位用户名及操作
        aa = driver.find_element_by_css_selector("input[alt*='邮箱']")
        aa.send_keys("hadoop")
        # 定位面框及操作
        driver.find_element_by_css_selector("input[alt*='密码']").send_keys("111111")
        # 点击登录按钮
        driver.find_element_by_css_selector(".submit_login").click()
        # 获取错误信息
        text = driver.find_element_by_css_selector(".prompt").text
        # 断言用户名密码错误
        try:
            # 为了能捕获断言异常，故意写错
            self.assertIn("密码不匹1配", text)
        except AssertionError:
            print("密码错误提示信息:", sys.exc_info())
            # 获取系统时间
            nowtime = time.strftime("%Y_%m_%d %H%M%S")
            # 截屏保存
            driver.get_screenshot_as_file("../Image/%s.jpg--%s"%(nowtime, sys.exc_info()[1]))
            # 抛出异常
            raise AssertionError

    def tearDown(self):
        sleep(2)
        # 关闭浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
