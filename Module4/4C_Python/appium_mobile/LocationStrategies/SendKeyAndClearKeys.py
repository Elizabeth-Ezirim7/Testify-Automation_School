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
        'appPackage': 'com.google.android.apps.maps',
        'appActivity': 'com.google.android.maps.MapsActivity ',
        'noSign': True
    }

    url = 'http://127.0.0.1:4723/wd/hub'

    driver = webdriver.Remote( url, options=AppiumOptions().load_capabilities( cap ) )
    time.sleep( 3 )
    # Locate By ID
    skip_button = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.Button[@text="SKIP"]' )
    skip_button.click()
    time.sleep( 2 )
    search_el = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Search here"]/android.widget.TextView' )
    search_el.click()
    search_here_box = driver.find_element(by=AppiumBy.ID, value="com.google.android.apps.maps:id/search_omnibox_edit_text")
    search_here_box.send_keys("Lagos")
    search_here_box.clear()
    time.sleep( 2 )
    print( "Clicked on Element" )
    driver.quit()


if __name__ == '__main__':
    main()


# com.google.android.apps.maps:id/search_omnibox_container