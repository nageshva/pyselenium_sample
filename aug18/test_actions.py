import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import pytest


def test_01_actions():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.NAME,"firstname")

    #now we have to do move curser and enter the name as Cap letters,to do that we have to use actions
    #for capital letters(use SHIFT +letters)

    #creating actions using object
    actions=ActionChains(driver)
    #here we are going to send keys with SHIFT buttom for caps
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"nagesh").key_up(Keys.SHIFT).perform()

    url=driver.find_element(By.XPATH,"//a[normalize-space()='Click here to Download File']")
    actions.context_click(url).perform() # to do right Click

    time.sleep(20)
    #
    # driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    # actions.send_keys("nageshva").perform()
    # time.sleep(20)

