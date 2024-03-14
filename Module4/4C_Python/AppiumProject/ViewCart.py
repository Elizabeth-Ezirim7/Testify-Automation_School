import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class DemoApp_ViewCart( unittest.TestCase ):

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

    def test_case_1_sort(self):
        sort_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        time.sleep( 2 )
        price_asc_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.view.ViewGroup[@content-desc="priceAsc"]' )
        price_asc_button.click()
        time.sleep( 5 )

        #   def test_case_3_add_cart(self):
        # item 1
        first_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[1]' )
        first_item.click()
        time.sleep( 3 )
        add_first_item = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID,
                                                   value='Add To Cart button' )
        add_first_item.click()
        time.sleep( 3 )
        # Rate item
        give_five_star = self.driver.find_element( by=AppiumBy.ACCESSIBILITY_ID,
                                                   value='review star 5' )
        give_five_star.click()
        time.sleep( 2 )
        close_modal = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="Close Modal button"]' )
        close_modal.click()
        time.sleep( 5 )
        self.driver.back()

        time.sleep( 3 )

        # item 2
        second_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[2]' )
        second_item.click()
        time.sleep( 3 )
        add_second_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_second_item.click()
        time.sleep( 5 )
        self.driver.back()

        # item 3
        third_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[3]' )
        third_item.click()
        time.sleep( 3 )
        add_third_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_third_item.click()
        time.sleep( 5 )
        self.driver.back()

        # item 4
        fourth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='(//android.view.ViewGroup[@content-desc="store item"])[4]' )
        fourth_item.click()
        time.sleep( 3 )
        add_fourth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fourth_item.click()
        time.sleep( 5 )
        self.driver.back()
        time.sleep( 3 )

        # item 5
        # Scroll to the element by finding the visible element first
        # Scroll Up (replace with desired direction: "down" or "up")
        # self.driver.execute_script( "mobile: scroll", {"direction": "up"} )
        self.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=800 )
        fifth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[5]' )
        fifth_item.click()
        time.sleep( 3 )
        add_fifth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_fifth_item.click()
        time.sleep( 2 )
        self.driver.back()

        # item 6

        sixth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[6]' )
        sixth_item.click()
        time.sleep( 3 )
        add_sixth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_sixth_item.click()
        time.sleep( 3 )

        # def test_case_4_view_cart(self):
        cart_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="cart badge"]' )
        cart_button.click()
        # time.sleep( 3 )

        # def test_case_5_assert(self):
        self.driver.swipe( start_x=500, start_y=1000, end_x=1000, end_y=1000, duration=800 )
        items_picked = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='//android.view.ViewGroup[@content-desc="checkout footer"]' )
        get_Attribute = items_picked.get_attribute( "content-desc" )
        print( "Content Attribute:", get_Attribute )
        expected_items = "6 items"
        actual_items = "6 items"

        if actual_items == expected_items:
            print( "Total no of items picked:", actual_items )
            assert actual_items == expected_items
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        # def test_case_6_remove_item(self):
        remove_item1 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item1.click()
        time.sleep( 3 )
        remove_item2 = self.driver.find_element( by=AppiumBy.XPATH,
                                                 value='(//android.view.ViewGroup[@content-desc="remove item"])[1]' )
        remove_item2.click()
        time.sleep( 5 )

        # def test_case_7_totalNo(self):
        items_left = self.driver.find_element( by=AppiumBy.XPATH, value="//android.widget.TextView[@text='4 items']" )
        get_Attribute = items_left.get_attribute( "text" )
        print( "Text Attribute:", get_Attribute )
        expected_items = "4 items"
        actual_items = "4 items"

        if actual_items == expected_items:
            print( "Total no of items left after removal is:", actual_items )
            assert actual_items == expected_items
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        proceed_checkout_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                            value='//android.view.ViewGroup[@content-desc="Proceed To Checkout button"]' )
        proceed_checkout_button.click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
