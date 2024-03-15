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

    keypad_el = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/fab' )
    keypad_el.click()
    # find by classname/Tagname
    frame_layout = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/dialpad' )
    number_buttons = frame_layout.find_elements(by=AppiumBy.CLASS_NAME, value="android.widget.LinearLayout")
    for number_button in number_buttons:
        number_button.click()
    time.sleep( 5 )
    driver.quit()


if __name__ == '__main__':
    main()
