import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_NewTab():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    #REGlink=Keys.CONTROL+Keys.RETURN
    # driver.find_element(By.XPATH,"//a[normalize-space()='Register']").send_keys(Keys.CONTROL+Keys.RETURN)


# now let see open diff urls in diff tabs
#     driver.switch_to.new_window("window") # if tab - open new tab,if window -new window open
#     driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    



    time.sleep(5)