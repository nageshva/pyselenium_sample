import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


def test_window():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert

    # Execute JavaScript to clear the text input field in the prompt dialog
    driver.execute_script("arguments[0].value = '';", alert)

    # Accept the prompt to confirm the changes
    alert.accept()



    time.sleep(5)


