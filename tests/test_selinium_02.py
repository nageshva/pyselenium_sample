import pytest

from selenium import webdriver

import logging

# chrome options
# to maximize window/install something/enable proxy/Js disabled

def test_login():

    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--headless=new") to hide UI Run in Browser
    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/")