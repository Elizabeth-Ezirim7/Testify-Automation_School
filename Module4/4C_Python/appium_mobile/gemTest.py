from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'platformVersion': '10',
    "appPackage": "com.google.android.apps.camera",
    "appActivity": ".activities.CameraActivity",
    "noSign": "True"
}

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities = desired_caps)
# Your test code here
    driver.quit()