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
        'appPackage': 'com.android.dialer',
        'appActivity': '.main.impl.MainActivity',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
    # time.sleep( 2 )
    # Locate By Xpath
    """"dialer_el = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Phone"]' )
    dialer_el.click()
    time.sleep( 2 )"""

    keypad_el = driver.find_element( by=AppiumBy.XPATH,
                                     value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                                           'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/'
                                           'android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout' )
    keypad_el.click()
    time.sleep( 5 )
    print( "Clicked on Element" )
    driver.quit()


if __name__ == '__main__':
    main()
