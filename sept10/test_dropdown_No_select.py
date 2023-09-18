import copy
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



def test_dropdown_No_select():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
    countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
    time.sleep(3)
    print(len(countries))

    for c in countries:
        if c.text=="Egypt":
            c.click()
            break

    time.sleep(3)



