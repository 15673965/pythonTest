from applium.find_element.capability import driver, check_cancle, check_skip

check_cancle()

check_skip()

# driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('zxw1234')
# driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('zxw123456')
# driver.find_element_by_xpath('//android.widget.Button').click()

# driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()


driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'用户名')]").send_keys('zxw1234')
# driver.find_element_by_xpath("//*[@class='android.widget.EditText' and @text='请输入密码']").send_keys('zxw123456')
driver.find_element_by_xpath('//*[@resource-id="com.tal.kaoyan:id/login_parent_layout"]/android.widget.LinearLayout/android.widget.EditText[2]').send_keys('zxw123456')
# eles = driver.find_elements_by_id("com.tal.kaoyan:id/login_parent_layout")
# print(len(eles))
driver.find_element_by_xpath('//*[@resource-id="com.tal.kaoyan:id/login_parent_layout"]/android.widget.LinearLayout/android.widget.Button').click()

driver.quit()