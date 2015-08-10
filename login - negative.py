from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
        
expected_error = 'You have entered an incorrect username or password.'
        
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.bitglass.com/'
        self.verificationerrors = []
        
    def test_login_with_wrong_pwd(self):
        driver = self.driver
        driver.get(self.base_url)
        
        #navigate to login page from the homepage
        driver.find_element_by_id('login-link').click()
        

        #email address
        username = driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys('cuiewu@gmail.com')
        
        #password
        password = driver.find_element_by_id('id_password')
        password.clear()
        password.send_keys('123456')
        
        #login button
        driver.find_element_by_id('id_login').click()
        
        #find the alert element
        alert = driver.find_element_by_xpath('.//div[@class="alert alert-error"]')
        
        # verify the text
        try:
            self.assertEqual(expected_error, alert.text)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationerrors)
        

if __name__ == '__main__':
    unittest.main()

