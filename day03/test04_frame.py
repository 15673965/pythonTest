# 导包
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
driver.maximize_window()
sleep(2)

# 输入注册信息
driver.find_element_by_css_selector("#user").send_keys("admin")
sleep(1)
driver.find_element_by_css_selector("#password").send_keys("123456")
sleep(1)
driver.find_element_by_css_selector("#tel").send_keys("18111265465")
sleep(1)
driver.find_element_by_css_selector("#email").send_keys("1188@qq.com")
sleep(1)

# 切换到注册A信息表单
driver.switch_to.frame("myframe1")
# 输入注册A信息
driver.find_element_by_css_selector("#userA").send_keys("admin")
sleep(1)
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
sleep(1)
driver.find_element_by_css_selector("#telA").send_keys("18111265465")
sleep(1)
driver.find_element_by_css_selector("#emailA").send_keys("1188@qq.com")
sleep(1)
# 切换之前需要先回到主页面，因为只有主页面含有注册B的frame
driver.switch_to.default_content()
# 切换到注册B信息表单
driver.switch_to.frame("myframe2")

# 输入注册B信息
driver.find_element_by_css_selector("#userB").send_keys("admin")
sleep(1)
driver.find_element_by_css_selector("#passwordB").send_keys("123456")
sleep(1)
driver.find_element_by_css_selector("#telB").send_keys("18111265465")
sleep(1)
driver.find_element_by_css_selector("#emailB").send_keys("1188@qq.com")
sleep(2)


driver.quit()

