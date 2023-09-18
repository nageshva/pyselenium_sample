import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Hmode():
    ops=webdriver.ChromeOptions()
    ops.headless=True # headless mode is helps to run the code without showing UI functionality parallelly to user
    driver = webdriver.Chrome(options=ops)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    print(driver.title)
    print(driver.current_url)