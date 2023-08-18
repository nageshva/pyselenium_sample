import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pytest


def test_actions():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    #click_ele=driver.find_element(By.XPATH,"//input[@id='clickable']") ...for input box
    #Click_hyper=driver.find_element(By.XPATH,"//a[@id = 'click']") ----for click on hyperlink
    #hov=driver.find_element(By.ID,"hover") ----for hovering on
    drag=driver.find_element(By.ID,"draggable")
    drop=driver.find_element(By.ID,"droppable")

    action=ActionChains(driver)

    #action.click_and_hold(click_ele).key_down(Keys.SHIFT).key_down("N").key_up(Keys.SHIFT).perform()
    #action.click_and_hold(Click_hyper).perform()
    #action.double_click(click_ele).perform()
    #action.drag_and_drop(drag,drop).perform()
    x=125
    y=313
    action.drag_and_drop(drag,drop).perform()

   # action.drag_and_drop_by_offset(drag, xoffset=x, yoffset=y).perform()  ----irregular placemnt of drag in drop
    time.sleep(10)

    #assert "resultPage.html" in driver.current_url

    #time.sleep(5)
