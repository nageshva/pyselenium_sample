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


    username_ele=driver.find_element(By.XPATH,"//div/input[@name='username']")
    username_ele.send_keys("Admin")

    password_ele=driver.find_element(By.XPATH,"//div/input[@name='password']")
    password_ele.send_keys("admin123")

    time.sleep(20)

    page_title=driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']")

    assert "Dashboard" in page_title



