from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


def main():
    desired_caps: Dict[str, Any] = {
        'platformName': 'Android',
        'platformVersion': "10",
        'deviceName': 'Android Emulator',
        'automationName': 'uiautomator2',
        'appPackage': 'com.android.camera2',
        'appActivity': 'com.android.camera.CaptureActivity',
        'noReset': True
    }

    appium_server_url = 'http://127.0.0.1:4723/wd/hub'

    # driver = webdriver.Remote( appium_server_url, desired_cap)
    # Include this line in your script to set the Appium server logs
    driver = webdriver.Remote( appium_server_url, options=AppiumOptions().load_capabilities( desired_caps ) )
    camera_button = driver.find_element( by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Camera"]' )
    camera_button.click()

    # camera_button = driver.find_element( AppiumBy.ACCESSIBILITY_ID, "Camera" )

    # camera_button = driver.find_element( AppiumBy.ACCESSIBILITY_ID, "Camera" )

    try:
        time.sleep( 5 )
        # Perform additional actions here, such as taking a photo, recording a video, etc.
        # For example, you can find elements by ID, class name, or other locators and interact with them.

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
