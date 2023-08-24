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
    url="https://www.flipkart.com/"
    driver.get(url)

    time.sleep(5)

    pop_up=driver.find_element(By.XPATH,"//button[contains(text(),'✕')]")
    pop_up.click()
    time.sleep(2)
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys('AC')


    search_svg_icon=driver.find_element(By.XPATH,"//*[local-name()='svg']//*[local-name()='g' and @fill-rule='evenodd']")
    actions=ActionChains(driver)
    actions.move_to_element(search_svg_icon).click().perform()

    time.sleep(5)
