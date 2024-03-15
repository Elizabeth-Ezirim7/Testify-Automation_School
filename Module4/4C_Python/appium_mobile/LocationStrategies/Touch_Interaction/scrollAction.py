import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy


def skip_page(driver):
    skip_button = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.Button[@text="SKIP"]')
    skip_button.click()


def scroll(driver):
    time.sleep(3)
    map_view = driver.find_element(by=AppiumBy.ID, value='com.google.android.apps.maps:id/explore_tab_home_bottom_sheet')
    actions = TouchAction( driver )
    actions.press(map_view, 500, 500, 1)
    actions.move_to( map_view, 200, 200)
    actions.release()
    actions.perform()


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
    skip_page( driver )
    scroll(driver)
    time.sleep( 5 )
    driver.quit()


if __name__ == '__main__':
    main()

# com.google.android.apps.maps:id/search_omnibox_container
