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
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
    time.sleep( 5 )
    # Locate By ID
    chrome_el = driver.find_element( by=AppiumBy.ID, value='com.android.chrome:id/signin_fre_dismiss_button' )
    chrome_el.click()
    time.sleep( 5 )
    print( "Clicked on Element" )
    driver.quit()


if __name__ == '__main__':
    main()
