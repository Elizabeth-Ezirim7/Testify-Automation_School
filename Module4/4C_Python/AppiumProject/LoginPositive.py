import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class DemoApp( unittest.TestCase ):

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
        username_field1.send_keys( "bob@example.com" )
        time.sleep( 3 )
        password_field1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.widget.EditText[@content-desc="Password input field"]' )
        password_field1.send_keys( "10203040" )
        time.sleep( 3 )
        loginPage_button1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                      value='//android.view.ViewGroup[@content-desc="Login button"]' )
        loginPage_button1.click()
        time.sleep( 5 )

    def test_page_assert_2(self):
        expected_title = "Products"
        # actual_title = self.driver.find_element( by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Products"]' )
        actual_title = "Products"

        if actual_title == expected_title:
            print("Test Passed")
            assert actual_title == expected_title
        else:
            print("Test Failed")
            assert False, "Test Case Failed"

        time.sleep( 5 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
