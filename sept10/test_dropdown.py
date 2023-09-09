import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dropdowns():
    driver=webdriver.Chrome()
    mywait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    countries=driver.find_element(By.XPATH,"//select[@id='country']")
    country=Select(countries)
    #country.select_by_visible_text("India")
    country_list=country.options
    for opt  in country_list:
        if opt.text=="India":
            opt.click()
          

