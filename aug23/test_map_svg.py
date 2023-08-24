import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_01_svg(driver):
    url="https://www.amcharts.com/svg-maps/?map=india"
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    action=ActionChains(driver)
    states_list=driver.find_elements(By.XPATH,"//*[local-name()='svg']/*[local-name()='g'][7]/*[local-name()='g']/*[local-name()='g']/*[local-name()='path']")
    for state in states_list:
        state_name=state.get_attribute('aria-label')
        print(state_name)
        if state_name== "Andhra Pradesh":
            action.move_to_element(state).click().perform()
            break
    time.sleep(10)