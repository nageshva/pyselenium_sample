import time

from selenium import webdriver



import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_01_login_pos():
    Logger=logging.getLogger(__name__)
    # create the session -webdriver
    driver=webdriver.Chrome()


    #Now I'm maximizing the window
    driver.maximize_window()
    #Now I'm navigating to URL
    driver.get("https://app.vwo.com/")

    #Now lets find the elements for email ,password fileds  and signup .

    email_ele= driver.find_element(By.ID,"login-username")
    pasword_ele= driver.find_element(By.ID,"login-password")

    signup_ele= driver.find_element(By.ID,"js-login-btn")

    #Now lets pass the date to those fields using sending keys

    email_ele.send_keys("93npu2yyb0@esiix.com")
    pasword_ele.send_keys("Wingify@123")

    signup_ele.click()

    # after this there is some delay to navigate to next page/next tab..hence we need some wait time ,now we can add Explicit wait here

    # for next tab title

    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"),"Dashboard")
    )

    page_heading_element = driver.find_element(By.CSS_SELECTOR, ".page-heading")
    assert "Dashboard" in page_heading_element.text


 #Now I want to check for negative testcase by giving invalid email/pswrd

def test_01_login_Neg():

    # create the session -webdriver
    driver = webdriver.Chrome()

    # Now I'm maximizing the window
    driver.maximize_window()
    # Now I'm navigating to URL
    driver.get("https://app.vwo.com/")

    # Now lets find the elements for email ,password fileds  and signup .

    email_ele = driver.find_element(By.ID, "login-username")
    pasword_ele = driver.find_element(By.ID, "login-password")

    signup_ele = driver.find_element(By.ID, "js-login-btn")
   # warn_ele  = driver.find_element(By.ID,"js-notification-box-msg")
    # Now lets pass the date to those fields using sending keys

    email_ele.send_keys("93npu2yyb0@esiix.com")
    pasword_ele.send_keys("Wingfy@123")

    signup_ele.click()

    time.sleep(1)
    #Now we will get warn pop up for invalid credentials
    notification_msg=driver.find_element(By.ID, "js-notification-box-msg")



    assert "Your email, password, IP address or location did not match" in notification_msg.text
    print(notification_msg.text)




#
#



