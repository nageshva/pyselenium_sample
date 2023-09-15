import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#


#static
def test_calender():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/datepicker/")

    # driver.find_element(By.ID,"datepicker").send_keys("09/12/2024")
    # time.sleep(3)
    year="2024"
    month="June"
    date="22"

    driver.switch_to.frame(0)
    driver.find_element(By.ID, "datepicker").click()
    # current_month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    # current_year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    # #print(current_year,current_month)

    while True:
        current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        # print(current_year,current_month)
        if current_year==year and current_month==month:
            break

        else:
            driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

    dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td[@data-handler='selectDay']")
    for ele in dates:
        if ele.text==date:
            ele.click()
            break
    time.sleep(5)

def test_DOB():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.find_element(By.XPATH,"//input[@id='dob']").click()
    Month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
    Month.select_by_visible_text("Jan")
    Year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
    Year.select_by_visible_text("1996")

    all_dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
    for ele in all_dates:
        if ele.text=="9":
            ele.click()
            break
    time.sleep(5)



