import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


def launch_chrome_session():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'app': 'C:\\Users\\EEzirim\\Documents\\Elizabeth\\AppiumFiles\\PersonalAPKs\\com.google.android.calculator_v8.2_(450571785)-82001598_Android-6.0.apk',
        'appPackage': 'com.google.android.calculator',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
    time.sleep( 5 )
    # Locate By Accessiblity ID
    # calculator_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='Calculator' )
    # calculator_el.click()
    number1_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='5' )
    number1_el.click()
    operator_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='multiply' )
    operator_el.click()
    number2_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='2' )
    number2_el.click()
    equality_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='equals' )
    equality_el.click()
    driver.get_screenshot_as_file("Total.png")
    print( "The answer is 10" )
    time.sleep(5)
    driver.quit()


def phone_dialer_session():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'appPackage': 'com.android.dialer',
        'appActivity': '.main.impl.MainActivity',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )

    keypad_el = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/fab' )
    keypad_el.click()
    # find by classname/Tagname
    frame_layout = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/dialpad' )
    number_buttons = frame_layout.find_elements( by=AppiumBy.CLASS_NAME, value="android.widget.LinearLayout" )
    for number_button in number_buttons:
        number_button.click()
    time.sleep( 5 )
    print("Dialer successfully launched")
    driver.get_screenshot_as_file( "Dialer.png" )
    driver.quit()


def main():
    launch_chrome_session()
    phone_dialer_session()


if __name__ == '__main__':
    main()
