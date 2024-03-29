#encoding=utf-8
from applium.page_object.common_fun import Common,logging
from applium.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):

    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')


    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('===============login===============')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished ')

if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('自学网2018','zxw2018')
