import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#lets check for invalid credentials
def test_HRM_login_Pos_01():
    driver=webdriver.Chrome()
    driver.maximize_window()

    #lets hit the url

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait=WebDriverWait(driver,5)
    wait.until(
        EC.visibility_of_element_located((By.XPATH,"//h5[normalize-space()='Login']"))
    )
    username_ele=driver.find_element(By.XPATH,"//div/input[@name='username']")
    username_ele.send_keys("Admin")

    password_ele=driver.find_element(By.XPATH,"//div/input[@name='password']")
    password_ele.send_keys("admin123")

    login_button=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
    login_button.click()

    wait.until(
        EC.text_to_be_present_in_element((By.XPATH,"//h6[normalize-space()='Dashboard']"),"Dashboard"))

   
    page_title=driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']")

    assert "Dashboard" in page_title.text



