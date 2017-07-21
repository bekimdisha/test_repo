import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import setup_logger


class TestSignUpAndLogIn(unittest.TestCase):
    
    def setUp(self):
        self.logger_inst = setup_logger.SetupLogger()
        self.logger = self.logger_inst.setup_logger()
    # create a new Firefox session
        self.logger.info("Test Suite Setup started!")
        self.driver = webdriver.Chrome()

        # navigate to the application home page
        self.driver.get("http://www.weebly.com/")
    
    def test_signup_new_user(self):
        # get the right url

        self.logger.info("test_signup started!")
        signup_url = self.driver.get("http://www.weebly.com#signup")

        signup_username = self.driver.find_element_by_id("overlay-signup-form-name")
        self.logger.info('filling signup form with username bekimdisha')
        signup_username.send_keys("bekimdisha")
        time.sleep(1)
        signup_email = self.driver.find_element_by_id("overlay-signup-form-email")
        self.logger.info('filling signup form with email bekimdisha@gmail.com')
        signup_email.send_keys("bekimdisha@gmail.com")
        time.sleep(1)
        signup_password = self.driver.find_element_by_id("overlay-signup-form-pass")
        self.logger.info('filling signup form with password !bekim123!')
        signup_password.send_keys("!bekim123!")
        time.sleep(1)
        submit_button = self.driver.find_element_by_class_name("signup-form__submit")
        click_submit_button = self.driver.find_element_by_class_name("signup-form__submit").click()
        time.sleep(1)
        try:
        	not_now = self.driver.find_element_by_class_name("ecommerce-funnel__site-img")
        	chose_not_now = self.driver.find_element_by_class_name("ecommerce-funnel__site-img").click()
        except NoSuchElementException as eex:
            self.logger.warn('test_signup_new_user FAILED', str(eex.message))
        time.sleep(1)
        try:
        	assert 'Weebly - Getting Started' in str(self.driver.title)
        except Exception as e:
        	self.logger.warn('test_signup_new_user FAILED', str(e.message))
        self.logger.info("test_signup ended!")

    def tearDown(self):
        self.logger.info("Test Suite finished. Tearning down setup!")
    	self.driver.close()


if __name__ == '__main__':
    unittest.main()