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

    def test_login(self):
        
        self.logger.info("test_login started!")
        login_url = self.driver.get("http://www.weebly.com#login")

        username = self.driver.find_element_by_id("weebly-username")
        self.logger.info('attempting to login with username bekimdisha@gmail.com')
        set_un = username.send_keys("bekimdisha@gmail.com")
        time.sleep(1)
        password = self.driver.find_element_by_id("weebly-password")
        self.logger.info('attempting to login with password !bekim123!')
        set_pass = password.send_keys("!bekim123!")
        time.sleep(1)
        login_button = self.driver.find_element_by_class_name("login-btn")
        click_login_btn = self.driver.find_element_by_class_name("login-btn").click()
        time.sleep(1)

        try:
        	assert 'Weebly - Getting Started' in str(self.driver.title)
        except Exception as e:
        	self.logger.warn('test_login FAILED', format(e))

        self.logger.info("test_login ended!")


    def tearDown(self):
        self.logger.info("Test Suite finished. Tearning down setup!")
    	self.driver.close()


if __name__ == '__main__':
    unittest.main()

