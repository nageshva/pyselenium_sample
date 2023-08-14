import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkbox():
    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/checkboxes")

    #box=driver.find_elements(By.XPATH,"//form[@id='checkboxes']")
    #
    # for c in box:
    #     if not c.is_selected():
    #         c.click()

    #for example if want to click the first box then my xpath will be
    box=driver.find_element(By.XPATH,"//input[@type= 'checkbox'][1]")
    box.click()

    time.sleep(10)

