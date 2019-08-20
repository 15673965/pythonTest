from applium.find_element.capability import driver, check_cancle, check_skip, NoSuchElementException
import time

def login():
    check_cancle()
    check_skip()
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").clear()
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext").send_keys("自学网2018")
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext").send_keys("zxw2018")
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn").click()

try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    login()
else:
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_userheader").click()
    login()

time.sleep(2)
driver.quit()