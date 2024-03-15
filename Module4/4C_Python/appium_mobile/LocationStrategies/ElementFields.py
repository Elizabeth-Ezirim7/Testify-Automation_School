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
    # Add Favorite
    add_fav_el = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/empty_list_view_action' )
    print("Text:", add_fav_el.text)
    print("Size:", add_fav_el.size)
    print("Location:", add_fav_el.location )
    print("Rectangle:", add_fav_el.rect)
    print("Is Enabled:", add_fav_el.is_enabled())
    print("Is Selected:", add_fav_el.is_selected() )
    print("Is Displayed:", add_fav_el.is_displayed() )
    time.sleep( 2 )


    # contact button
    contact_button_el = driver.find_element(by=AppiumBy.ID, value='com.android.dialer:id/contacts_tab')
    print( "\n\nText:", contact_button.el.text )
    print( "Size:", contact_button_el.size )
    print( "Location:", contact_button_el.location )
    print( "Rectangle:", contact_buttont_el.rect )
    print( "Is Enabled:", contact_buttont_el.is_enabled() )
    print( "Is Selected:", contact_button_el.is_selected() )
    print( "Is Displayed:", contact_button_el.is_displayed() )
    contact_button_el.click()
    time.sleep( 2 )

    # create contact
    create_contact_el = driver.find_element( by=AppiumBy.ID, value='com.android.dialer:id/empty_list_view_action' )
    print( "\n\nText:", create_contact_el.text )
    print( "Size:", create_contact_el.size )
    print( "Location:", create_contact_el.location )
    print( "Rectangle:", create_contact_el.rect )
    print( "Is Enabled:", create_contact_el.is_enabled() )
    print( "Is Selected:", create_contact_el.is_selected() )
    print( "Is Displayed:", create_contact_el.is_displayed() )
    time.sleep( 2 )
    driver.quit()


if __name__ == '__main__':
    main()
