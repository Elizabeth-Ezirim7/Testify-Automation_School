import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class NegativeLoginTest( unittest.TestCase ):

    @classmethod
    def setUp(cls):
        cap: Dict[str, Any] = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android',
            'app': 'C:\\Users\\EEzirim\\Documents\\Elizabeth\\TestifyAPK\\Android-MyDemoAppRN.1.1.0.build-226.apk',
            'appPackage': 'com.saucelabs.mydemoapp.rn',
            'appActivity': '.MainActivity',
            'noSign': True
        }

        url = 'http://127.0.0.1:4723/wd/hub'

        cls.driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
        time.sleep( 5 )

    def test_case_1(self):
        hamburger_icon = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='open menu' )
        hamburger_icon.click()
        login_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                             value='//android.view.ViewGroup[@content-desc="menu item log in"]' )
        login_button1.click()
        time.sleep( 5 )
        # driver.find_element(by=AppiumBy.XPATH, value='//android.view.ViewGroup[@content-desc="login screen"]').is_displayed()
        username_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "Elizabeth" )
        time.sleep( 3 )
        password_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "Test123$" )
        time.sleep( 3 )
        loginPage_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 2 )
        invalid_credentials_msg1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "invalid username and invalid password:", get_Attribute1 )
        time.sleep( 3 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 5 )

        # def test_case_2(self):
        # 2nd negative login test case
        # Login with invalid username and valid password
        """"hamburger_icon = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='open menu' )
        hamburger_icon.click()
        login_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@content-desc="menu item log in"]' )
        login_button1.click()
        time.sleep( 5 )"""""
        username_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "Elizabeth" )
        password_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        invalid_credentials_msg1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "invalid username and valid password:", get_Attribute1 )
        time.sleep( 3 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 5 )

        # def test_case_3(self):
        # 3rd negative login test case
        # Login with valid username and invalid password
        """"hamburger_icon = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='open menu' )
        hamburger_icon.click()
        login_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@content-desc="menu item log in"]' )
        login_button1.click()
        time.sleep( 5 )"""""
        username_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "bob@example.com" )
        password_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040rrr" )
        time.sleep( 3 )
        loginPage_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        invalid_credentials_msg1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.view.ViewGroup[@content-desc="generic-error-message"]/android.widget.TextView' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "valid username and invalid password:", get_Attribute1 )
        time.sleep( 3 )
        username_field1.clear()
        password_field1.clear()
        time.sleep( 5 )

        # def test_case_4(self):
        # 4th negative login test case
        # Login with empty username and valid password
        """"hamburger_icon = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='open menu' )
        hamburger_icon.click()
        login_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@content-desc="menu item log in"]' )
        login_button1.click()
        time.sleep( 5 )"""""
        username_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Username input field"]' )
        username_field1.send_keys( "" )
        password_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 3 )
        invalid_credentials_msg1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Username is required"]' )
        get_Attribute1 = invalid_credentials_msg1.get_attribute( "text" )
        print( "Empty Username:", get_Attribute1 )
        print( invalid_credentials_msg1.is_displayed() )
        time.sleep( 3 )
        password_field1.clear()
        time.sleep( 5 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
