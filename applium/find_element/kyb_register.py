import random
import time

from applium.find_element.capability import driver, check_cancle, check_skip, NoSuchElementException


def register():
    # 进入注册界面选择并设置头像
    time.sleep(2)
    driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
    time.sleep(2)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
    time.sleep(2)
    driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[1].click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[contains(@text,"保存") and @class="android.widget.Button"]').click()
    time.sleep(2)
    # 注册信息填写
    username = "zxw2019" + "FLY" + str(random.randint(1000, 9999))
    print(username)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
    time.sleep(2)

    password = 'zxw' + str(random.randint(1000, 9000))
    print('password: %s' % password)
    # driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
    driver.find_element_by_android_uiautomator \
        ('new UiSelector().resourceId("com.tal.kaoyan:id/activity_register_password_edittext")').send_keys(password)
    time.sleep(2)

    email = '51zxw' + str(random.randint(1000, 9000)) + '@163.com'
    print('email: %s' % email)
    # driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
    driver.find_element_by_android_uiautomator \
        ('new UiSelector().resourceId("com.tal.kaoyan:id/activity_register_email_edittext")').send_keys(email)
    time.sleep(2)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

    # 院校选择
    driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
    # 选择省份
    driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()
    # 选择具体院校--同济大学
    driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()

    # 专业选择

    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
    # 选择经济学类-统计学-经济统计学
    driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
    driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
    driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()
    # 点击“进入考研帮”按钮
    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()


if __name__ == '__main__':
    check_cancle()
    check_skip()
try:
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
except NoSuchElementException:
    register()
else:
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl").click()
    time.sleep(2)
    driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_userheader").click()
    register()
