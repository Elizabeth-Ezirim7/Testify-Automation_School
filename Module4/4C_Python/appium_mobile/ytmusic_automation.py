import time
import unittest

# from typing import Dict
from appium import webdriver
# from selenium.webdriver.chrome import options
# from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.by import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    deviceName="Android Emulator",
    platformName="Android",
    platformVersion="10",
    appPackage="com.google.android.apps.camera",
    appActivity=".activities.CameraActivity",
    noSign="True"
)
appium_server_url = 'http://127.0.0.1:4723'


class TestAppium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(appium_server_url, capabilities)
        # self.driver = webdriver.Remote(appium_server_url, options=AndroidEmulator().load_capabilities(capabilities))

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Camera"]')
        el.click()

    """"deviceOnlyElement = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (MobileBy.XPATH, "//android.widget.Button[@text='DEVICE FILES ONLY']")))
    deviceOnlyElement.click()"""""
    time.sleep(5)
    #self.driver.quit()


if __name__ == '__main__':
    unittest.main()
