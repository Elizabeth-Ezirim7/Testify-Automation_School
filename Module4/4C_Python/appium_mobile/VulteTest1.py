from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support import By
from appium.webdriver.common.appiumby import By

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'platformVersion': '10',
    'automationName': 'uiautomator2',
    'deviceName': '2268a860c00d7ece',
    'appPackage': 'com.vulte.app',
    'appActivity': '.MainActivity'
}

url = 'http://127.0.0.1:4723/wd/hub'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
wait = WebDriverWait(driver, 10)
vulte_el = wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, 'VULTe')))
# vulte_el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='VULTe')
# vulte_el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="VULTe"]')
vulte_el.click()
driver.quit()
