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
        'appActivity': 'main.impl.MainActivity',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
    time.sleep( 5 )
    # Locate By Xpath
    contacts_el = driver.find_element( by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                                'android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/'
                                                                'android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.ImageView' )
    contacts_el.click()
    time.sleep( 5 )
    print( "Clicked on contact button" )
    Add_favorite_el= driver.find_element( by=AppiumBy.XPATH, value='//android.widget.TextView[@text="CREATE NEW CONTACT"]' )
    Add_favorite_el.click()
    print( "Clicked on Add favorite button" )
    time.sleep( 5 )
    cancel_button_el = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Cancel"]' )
    cancel_button_el.click()
    print( "Clicked on cancel button successfully" )
    driver.quit()


if __name__ == '__main__':
    main()
# C:\Users\EEzirim\AppData\Local\Android\Sdk\emulator //android.widget.ImageButton[@content-desc="Cancel"]