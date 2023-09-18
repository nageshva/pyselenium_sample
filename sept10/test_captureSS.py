import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dropdown_No_select():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    time.sleep(5)
    driver.save_screenshot("C:\\Users\\yours\\PycharmProjects\\Pyselenium\\sept10\\homapage.png")
    driver.quit()