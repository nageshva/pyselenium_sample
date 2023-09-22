import openpyxl

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from sept10 import ExcelUtilties


def test_SBIFD_Calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

    file="C:\\Users\\yours\\Desktop\\New.xlsx"
    rows=ExcelUtilties.getRowcount(file,"Sheet1")
#first fetch the test data from Excel sheet
    for r in range(2,rows+1):
        priniple=ExcelUtilties.readData(file,"Sheet1",r,1)
        rateofInterest=ExcelUtilties.readData(file,"Sheet1",r,2)
        per1=ExcelUtilties.readData(file,"Sheet1",r,3)
        per2=ExcelUtilties.readData(file, "Sheet1",r, 4)
        freq=ExcelUtilties.readData(file,"Sheet1",r,5)
        maturevalue=ExcelUtilties.readData(file,"Sheet1",r,6)

#Now pass the data to the application for that we have to  find out the elements
        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(priniple)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
        driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
        tenure_period=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
        tenure_period.select_by_visible_text(per2)
        frequency=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
        frequency.select_by_visible_text(freq)
        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click() # calucualte button
        result=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #Now let see the validation
        if float(maturevalue)==float(result):
            print('test is passed')
            ExcelUtilties.writeData(file,"Sheet1",r,8,"Passed")
            ExcelUtilties.fillGreenColor(file,"Sheet1",r,8)
        else:
            print('test is failed')
            ExcelUtilties.writeData(file, "Sheet1", r, 8, "Passed")
            ExcelUtilties.fillRedColor(file, "Sheet1", r, 8)


        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()

        time.sleep(10)

    driver.close()






