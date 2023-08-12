from selenium import webdriver

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_verify_login_neg():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()

    time.sleep(3)

    username1=driver.find_element(By.ID,"txt-username")
    username1.send_keys("xyz@gmail.com")

    password1 = driver.find_element(By.ID, "txt-password")
    password1.send_keys("35355")

    login=driver.find_element(By.ID,"btn-login")
    login.click()

    #time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, "p.lead.text-danger")
    assert "Login failed! " in error_message.text


def test_verify_login_pos():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()

    time.sleep(3)

    username1=driver.find_element(By.ID,"txt-username")
    username1.send_keys("John Doe")

    password1 = driver.find_element(By.ID, "txt-password")
    password1.send_keys("ThisIsNotAPassword")

    login=driver.find_element(By.ID,"btn-login")
    login.click()

    dropdown=Select(driver.find_element(By.ID,"combo_facility"))
    dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

    driver.find_element(By.ID,"chk_hospotal_readmission").click()
    driver.find_element(By.ID,"radio_program_medicaid").click()
    driver.find_element(By.ID,"txt_visit_date").send_keys("09/09/2023")
    driver.find_element(By.ID,"txt_comment").send_keys("Fever ")

    driver.find_element(By.ID,"btn-book-appointment").click()

    time.sleep(1)

    confirmation_message=driver.find_element(By.TAG_NAME,"h2")

    assert  "Appointment Confirmation" in confirmation_message.text



