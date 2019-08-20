from selenium import webdriver
from time import sleep
# 实例化浏览器
driver = webdriver.Firefox()
# 打开页面
driver.get(r"F:\BaiduYunDownload\webdriverspace\sources\注册实例.html")
sleep(2)

# 获取用户名文本框大小
size = driver.find_element_by_id("user").size
print("文本大小为: ", size)
# 获取文本值
text = driver.find_element_by_link_text("访问 新浪 网站").text
print("a标签链接文本值为: ", text)
# 获取元素属性值
attribute = driver.find_element_by_link_text("访问 新浪 网站").get_attribute("href")
print("a标签href属性值为: ", attribute)
print("------------------------------------")
# 获取当前页面title
print("当前页面title： ", driver.title)
# 获取当前页面url
print("当前页面url: " + driver.current_url)
print("------------------------------------")
# 判断span元素是否显示
is_displayed = driver.find_element_by_css_selector("span").is_displayed()
print("span元素是否显示：", is_displayed)
# 判断取消按钮是否可用
is_enabled = driver.find_element_by_css_selector("#cancel").is_enabled()
print("取消按钮是否可用：", is_enabled)

sleep(3)
driver.quit()