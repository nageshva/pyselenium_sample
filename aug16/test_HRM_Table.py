import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


def test_Webtable():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='Login']"))
    )
    username_ele = driver.find_element(By.XPATH, "//div/input[@name='username']")
    username_ele.send_keys("Admin")

    password_ele = driver.find_element(By.XPATH, "//div/input[@name='password']")
    password_ele.send_keys("admin123")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, "//h6[normalize-space()='Dashboard']"), "Dashboard"))

    page_title = driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")

    assert "Dashboard" in page_title.text

    #//div[@role='table']/div[2]/div[1]/div/div[4]/preceding-sibling::div[1]
    # driver.implicitly_wait(5)

    # Find the PIM menu and click it
    pim_menu = driver.find_element(By.XPATH,"//span[normalize-space()='PIM']")
    pim_menu.click()

    time.sleep(5)

    fp="//div[@role='table']/div/div["
    sp="]/div/div["
    tp="]"

    for i in range(1,10):
        for j in range(2,5):
            dynamic_path=f"{fp}{i}{sp}{j}{tp}"
            data=driver.find_element(By.XPATH,dynamic_path)
            print(data.text)

    time.sleep(2)