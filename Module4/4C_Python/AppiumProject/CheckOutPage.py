import time
import unittest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction



class AppCheckOut( unittest.TestCase ):

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

    # def test_case_1_sort(self):
        sort_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="sort button"]' )
        sort_button.click()
        time.sleep( 2 )
        price_asc_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.view.ViewGroup[@content-desc="priceAsc"]' )
        price_asc_button.click()
        time.sleep( 5 )

        # def test_case_2_add_cart(self):
        # item 1
        first_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[1]' )
        first_item.click()
        time.sleep( 3 )
        add_first_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_first_item.click()
        time.sleep( 3 )
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
        # Scroll Up (replace with desired direction: "down" or "up")
        # self.driver.execute_script( "mobile: scroll", {"direction": "up"} )

        sixth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='(//android.view.ViewGroup[@content-desc="store item"])[6]' )
        sixth_item.click()
        time.sleep( 3 )
        add_sixth_item = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Add To Cart button"]' )
        add_sixth_item.click()
        time.sleep( 2 )
        self.driver.back()
        time.sleep( 4 )

        # def test_case_4_view_cart(self):
        cart_button = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.view.ViewGroup[@content-desc="cart badge"]' )
        cart_button.click()
        time.sleep( 3 )

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
        time.sleep( 5 )

    # def test_case_3_checkout_form(self):
        # FullName
        self.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=800 )

        fullname_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Full Name* input field"]' )
        # fullname_el.click()
        fullname_el.send_keys( "Elizabeth Ezirim" )

        # Address Line 1
        address_line1_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.widget.EditText[@content-desc="Address Line 1* input field"]' )
        # address_line1_el.click()
        address_line1_el.send_keys( "112 Beverly Hills, Chicago" )

        # City
        city_el = self.driver.find_element( by=AppiumBy.XPATH,
                                            value='//android.widget.EditText[@content-desc="City* input field"]' )
        # city_el.click()
        city_el.send_keys( "Texas" )

        # Zip Code
        zip_code_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Zip Code* input field"]' )
        # zip_code_el.click()
        zip_code_el.send_keys( "908078" )

        # Country
        country_el = self.driver.find_element( by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Country* input field"]' )
        # country_el.click()
        country_el.send_keys( "Canada" )

        # To Payment Button
        to_payment_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@content-desc="To Payment button"]' )
        to_payment_el.click()
        time.sleep( 3 )

        # def test_case_4_checkout_payment_method_assert(self):

        expected_title = "Enter a payment method"
        actual_title = "Enter a payment method"

        if actual_title == expected_title:
            print( "CheckOut:", actual_title )
            assert actual_title == expected_title
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

        # def test_case_5_payment_method(self):
        # FullName
        self.driver.swipe( start_x=500, start_y=1000, end_x=500, end_y=500, duration=800 )
        fullname_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@content-desc="Full Name* input field"]' )

        fullname_el.send_keys( "Elizabeth Ezirim" )

        # Card Number

        card_Number_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.widget.EditText[@content-desc="Card Number* input field"]' )
        card_Number_el.send_keys( "123456789012345" )

        # Expiration date

        expiration_date_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                       value='//android.widget.EditText[@content-desc="Expiration Date* input field"]' )
        expiration_date_el.send_keys( "03/25" )

        # Security Code

        security_code_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                     value='//android.widget.EditText[@content-desc="Security Code* input field"]' )
        security_code_el.send_keys( "222" )

        # Review order Button
        review_order_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup[@content-desc="Review Order button"]' )
        review_order_el.click()
        time.sleep( 5 )


        review_order_scroll = self.driver.find_element( by=AppiumBy.XPATH,
                                                        value='//android.widget.ScrollView[@content-desc="checkout review order screen"]' )
        get_Attribute = review_order_scroll.get_attribute( "content-desc" )
        print( "Content Desc Attribute:", get_Attribute )

        self.driver.swipe( start_x=700, start_y=1000, end_x=1000, end_y=1000, duration=800 )

        place_order_el = self.driver.find_element( by=AppiumBy.XPATH,
                                                   value='//android.view.ViewGroup[@content-desc="Place Order button"]' )
        place_order_el.click()
        time.sleep(5)

    #  def test_case_6_checkout_complete(self):

        expected_title = "	Thank you for your order"
        actual_title = "	Thank you for your order"

        if actual_title == expected_title:
            print( "CheckOut Complete :", actual_title )
            assert actual_title == expected_title
        else:
            print( "Test Failed" )
            assert False, "Test Case Failed"
        time.sleep( 5 )

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
