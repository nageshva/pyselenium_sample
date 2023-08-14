import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_alerts_01():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
    button.click()

    #after clicking button we are getting alert window after few sec,so we will add time here

    wait=WebDriverWait(driver,10)
    wait.until(
        EC.alert_is_present()

    )

    alert=driver.switch_to.alert
    alert.accept()

    result=driver.find_element(By.XPATH,"//p[@id='result']")

    print(result.text)
    assert "You successfully clicked an alert" in result.text

def test_alerts_02():
    driver=webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")




    button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
    button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.alert_is_present()

    )
    alert=driver.switch_to.alert
    alert.accept()

    result=driver.find_element(By.XPATH,"//p[@id='result']")

    print(result.text)

    assert "You clicked: Ok" in result.text

def test_alerrts_03():

    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
    button.click()
    wait=WebDriverWait(driver,5)
    wait.until(EC.alert_is_present())

    alert=driver.switch_to.alert
    alert.send_keys("Nagesh")

    alert.accept()

    result=driver.find_element(By.XPATH,"//p[@id='result']")
    print(result.text)


