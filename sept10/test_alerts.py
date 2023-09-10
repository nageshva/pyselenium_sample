import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_window():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
    alert_window=driver.switch_to.alert
    # alert_window.clear()


    alert_window.send_keys("hello")
    time.sleep(10)
    alert_window.accept()


