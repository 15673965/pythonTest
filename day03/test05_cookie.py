from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.add_cookie({'name': 'BAIDUID', 'value': '67D051BC49FFEBB016846620CE32E1A7'})
driver.add_cookie({'name': 'BDUSS', 'value': 'EZEbTVNV3F6Vk5oZnZKMm1PQnliWWV-ZDAwUkxESWgtOTZCaDNxa0pNWWRDelZkSVFBQUFBJCQAAAAAAAAAAAEAAAC7dXOjc2MxNTY3Mzk2NQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB1-DV0dfg1dV'})
# 打印cookies
print("-----------------------------------------------")
cookies = driver.get_cookies()
print(cookies)
print("-----------------------------------------------")
for cookie in cookies:
    print("%s--------->%s"%(cookie["name"], cookie["value"]))
# 获取指定cookie
'''
print("-----------------------------------------------")
BAIDUID = driver.get_cookie("BAIDUID")
BDUSS = driver.get_cookie("BDUSS")
print("BAIDUID: ", BAIDUID)
print("BDUSS: ", BDUSS)
print("-----------------------------------------------")
'''
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()