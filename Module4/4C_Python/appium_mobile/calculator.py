from typing import Dict, Union

from appium import webdriver

from appium.webdriver.capabilities.capabilities import DesiredCapabilities


def Calulator():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'platformVersion': '10',
        "app": "C:\\Users\\EEzirim\\Documents\\Elizabeth\\AppiumFiles\\PersonalAPKs\\Calculator_8.4.1 (520193683)_Apkpure.apk",
        # "app": "https://127.0.0.1:9009//Calculator_8.4.1 (520193683)_Apkpure.apk",
        "appPackage": "com.google.android.calculator",

        "noSign": True
    }

    # Create a DesiredCapabilities instance and set capabilities
    options = webdriver.DesiredCapabilities()
    options.update(desired_caps)

    # Convert options to capabilities
    capabilities = options.to_capabilities()

    # Appium server address
    # 192.168.43.209
    appium_server_url = 'http://192.168.43.209:4723/wd/hub'
    # appium_server_url = 'http://localhost:4723/wd/hub'

    driver = webdriver.Remote(appium_server_url, capabilities)

    # driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub")
    # Your test code here
    driver.quit()


if __name__ == '__main__':
    Calulator()
