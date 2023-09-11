import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtable():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
    time.sleep(5)

    #//div[@class='oxd-table orangehrm-employee-list']//div[@class='oxd-table-card'][]//div[@role='row']
    #//div[@class='oxd-table-header']//div[@role='columnheader'][]

    rows=driver.find_elements(By.XPATH,"//div[@class='oxd-table orangehrm-employee-list']//div[@class='oxd-table-card']//div[@role='row']")
    cols=driver.find_elements(By.XPATH,"//div[@role='table']/div[2]/div[1]/div/div")
    print(len(rows),len(cols))

    count = 0
    for i in range(1,len(rows)):

        first_name=driver.find_element(By.XPATH,"//div[@role='table']/div[2]/div["+str(i)+"]/div/div[3]").text

        job_title=driver.find_element(By.XPATH,"//div[@role='table']/div[2]/div["+str(i)+"]/div/div[5]").text
        if job_title=="QA Engineer":

            print("Hi I'm ",first_name ,"Im doing ",job_title)
            count+=1
    print("No of QA are ",count)