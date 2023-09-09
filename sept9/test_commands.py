from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

def test_pycommands():
    driver=webdriver.Chrome()
    mywait=WebDriverWait(driver,10)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    register=mywait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".ico-register")))
    register.click()
