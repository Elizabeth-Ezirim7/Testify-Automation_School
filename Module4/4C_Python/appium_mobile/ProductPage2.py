import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class AppShoppingCart( unittest.TestCase ):

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

    def test_add_items_to_cart(self):
        # List of items to add to the cart
        items_to_add = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6']

        for item in items_to_add:
            # Perform actions to navigate to the item details page
            self.navigate_to_item_details( item )

            # Add the item to the cart
            self.add_item_to_cart()

            # Navigate back to the list of items or continue to the next item

        # Perform additional verifications if needed

    def navigate_to_item_details(self, item):
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
        sort_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        asc_button = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.view.ViewGroup[@content-desc="nameAsc"]' )
        asc_button.click()
        first_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.view.ViewGroup[@content-desc="store item"])[1]' )
        first_item.click()

    def add_item_to_cart(self):
        add_item = self.driver.find_element( by=AppiumBy.XPATH,
                                             value='//android.view.ViewGroup[ @ content - desc = "Add To Cart button"]' )
        add_item.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
