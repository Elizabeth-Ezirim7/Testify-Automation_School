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
    time.sleep( 5 )
    # Locate By ID
    add_fav_el = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/empty_list_view_action' )
    get_Attribute1 = add_fav_el.get_attribute("package")
    get_Attribute2 = add_fav_el.get_attribute( "resource-id" )
    get_Attribute3 = add_fav_el.get_attribute( "bounds" )
    print("Package Attribute:", get_Attribute1)
    print("Resource-Id Attribute:",  get_Attribute2 )
    print("Bounds Attribute:", get_Attribute3 )
    time.sleep( 5 )
    driver.quit()


if __name__ == '__main__':
    main()
