from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
}

url = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
battery_el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
battery_el.click()
print("The battery icon has been clicked on")

driver.quit()
