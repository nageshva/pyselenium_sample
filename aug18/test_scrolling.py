import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import pytest


def test_scroll():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    frame=driver.find_element(By.TAG_NAME,'iframe')
    #ActionChains(driver).scroll_to_element(frame).perform() ---full scroll

    #now let suppose we want to scroll inside of scrolling window and with that too offset ..means some x,y coordinates
    origin=ScrollOrigin.from_element(frame)
    ActionChains(driver).scroll_from_origin(origin,0,200).perform()

    time.sleep(30)