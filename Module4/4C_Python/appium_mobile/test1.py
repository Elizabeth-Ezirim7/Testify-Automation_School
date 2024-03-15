from appium import webdriver
import time
# from selenium.webdriver import Remote


# from appium.webdriver.common.mobileby import MobileBy

# Desired capabilities for your mobile device
def main():
    desired_caps = {
        'platformName': 'Android',  # or 'iOS' for iPhone
        'platformVersion': '10',
        'deviceName': 'Android Emulator',
        'appPackage': 'com.google.android.apps.camera',  # Package name for the camera app
        'appActivity': '.CameraActivity',  # Activity name for the camera app
        'noReset': True
    }

    # Appium server address
    appium_server_url = 'http://127.0.0.1.209:4723/wd/hub'

    # Initialize the driver
    driver = webdriver.Remote(appium_server_url, desired_caps)

    try:
        # Wait for a few seconds to allow the camera app to launch
        time.sleep(5)

    # You can perform additional actions here, such as taking a photo, recording a video, etc.
    # For example, you can find elements by ID, class name, or other locators and interact with them.

    finally:
        # Close the driver session
        driver.quit()
