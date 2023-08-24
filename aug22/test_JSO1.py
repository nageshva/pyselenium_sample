import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_js_execute(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    js_ext=driver.execute_script
    element=driver.find_element(By.CSS_SELECTOR,"button[onclick='addElement()']")
    js_ext("arguments[0].click()",element)
    #document.querySelector("button[onclick='addElement()']").click()
    time.sleep(4)

    driver.get("https://thetestingacademy.com/")
    js_ext("window.scrollBy(0,600)")
    time.sleep(3)