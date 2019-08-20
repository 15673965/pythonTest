# 导包
from time import sleep
from selenium import webdriver

# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
driver.maximize_window()
sleep(2)

# 定位注册A按钮并点击
driver.find_element_by_link_text("注册A网页").click()

# 获取当前敞口句柄
current_handle = driver.current_window_handle
print("当前敞口句柄：", current_handle)

# 获取所有窗口句柄
handles = driver.window_handles
print("所有敞口句柄：", handles)

# 遍历及切换

for handle in handles:
    if current_handle != handle:
        # 执行切换窗口方法
        driver.switch_to.window(handle)
        # 填写注册A信息
        # 输入注册A信息
        driver.find_element_by_css_selector("#userA").send_keys("admin")
        sleep(1)
        driver.find_element_by_css_selector("#passwordA").send_keys("123456")
        sleep(1)
        driver.find_element_by_css_selector("#telA").send_keys("18111265465")
        sleep(1)
        driver.find_element_by_css_selector("#emailA").send_keys("1188@qq.com")
        # 截图并保存
        driver.get_screenshot_as_file("../image/imag01.jpg")
sleep(2)
driver.quit()

