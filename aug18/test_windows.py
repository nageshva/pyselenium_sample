import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pytest


def test_Window():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    time.sleep(5)

    main_window=driver.current_window_handle
    print(main_window)
    link=driver.find_element(By.LINK_TEXT,'Click Here')
    link.click()

    time.sleep(10)

    windows=driver.window_handles
    print(windows)

    for window in windows:
        driver.switch_to.window(window)
        if "New Window" in driver.page_source:
            print("Yes present")
            break





