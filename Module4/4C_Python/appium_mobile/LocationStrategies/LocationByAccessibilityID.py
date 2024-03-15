import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


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
    print( "The answer is 10" )

    driver.quit()


if __name__ == '__main__':
    main()
