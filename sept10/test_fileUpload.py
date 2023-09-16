import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os




def test_file_Upload():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    time.sleep(5)
    img_Upload = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus']")

    img_Upload.click()
    time.sleep(5)
    upload=driver.find_element(By.XPATH,"//img[@class='employee-image']")
    upload.send_keys(os.getcwd()+"/Screenshot(1).png")
    time.sleep(5)
    #"C:\Users\yours\Desktop\my pic.jpg"
