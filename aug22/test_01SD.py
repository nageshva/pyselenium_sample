import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    # Read a File, Read from DB, Create Webdriver


@pytest.mark.usefixtures("driver")
def test_js_execute(driver):
    URL = "https://selectorshub.com/xpath-practice-page/"
    driver.get(URL)
    time.sleep(2)

    pizza_scroll=driver.execute_script("window.scrollBy(0,600)")
    time.sleep(2)
    # pizza=driver.execute_script( "return document.querySelector('#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza')")
    # pizza.send_keys("Farmhouse")
    youtube_link=driver.execute_script("return document.querySelector('#userName').shadowRoot.querySelector('.learningHub').click()")
    time.sleep(5)