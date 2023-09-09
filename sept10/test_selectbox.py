from selenium import webdriver
from selenium.webdriver.common.by import By

def test_select():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    checkboxs=driver.find_elements(By.XPATH,"//div[@class='form-group']//div[@class='form-check form-check-inline']//input[contains(@type,'checkbox')]")
    print(len(checkboxs))##7
    for i in range (0,len((checkboxs))):
         checkboxs[i].click()
