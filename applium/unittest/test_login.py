#encoding=utf-8
from applium.unittest.myunit import StartEnd
from applium.page_object.loginView import LoginView,logging
import unittest

class TestLogin(StartEnd):


    def test_login_zxw2018(self):
        logging.info('=========test_login_zxw2018============')
        l=LoginView(self.driver)
        l.login_action('自学网2018','zxw2018')


    def test_login_zxw2017(self):
        logging.info('==========test_login_zxw2017========')
        l=LoginView(self.driver)
        l.login_action('自学网2017','zxw2017')


    def test_login_error(self):
        logging.info('=======test_login_error=========')
        l=LoginView(self.driver)
        l.login_action('666','222')


if __name__ == '__main__':
    unittest.main()
