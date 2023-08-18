import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_make_my_trip():
    driver=webdriver.Chrome()


    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    time.sleep(5)
    boarding = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(boarding).click().send_keys("Hyderabad").perform()
    time.sleep(10)













