import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains


def main():
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

    actions = ActionChains(driver)
    number1_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='5')
    time.sleep(5)
    # move to element method
    """actions.move_to_element(number1_el)
    actions.click()
    actions.perform()"""
    # move_to_element_with_offset(number1_el, 200, 200)
    """"actions.move_to_element_with_offset(number1_el, 200, 200)
    actions.click()
    actions.perform()"""""
    # double click action
    """"actions.double_click(number1_el)
    actions.perform()"""""
    # click and hold and release method
    actions.click_and_hold(number1_el)
    actions.release()
    actions.perform()
    time.sleep( 5 )

    driver.quit()

    """"number1_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='5' )
    number1_el.click()
    operator_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='multiply' )
    operator_el.click()
    number2_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='2' )
    number2_el.click()
    equality_el = driver.find_element( by=AppiumBy.ACCESSIBILITY_ID, value='equals' )
    equality_el.click()
    print( "The answer is 10" )"""""



if __name__ == '__main__':
    main()
