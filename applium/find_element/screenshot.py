from applium.find_element.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('55555')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')

driver.save_screenshot('login.png') # 保存在当前脚本所在目录
driver.get_screenshot_as_file('./images/login.png') # 将截图保留到指定文件路径

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
