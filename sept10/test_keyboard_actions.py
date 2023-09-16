import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_keyboard():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://text-compare.com/")
    input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
    input1.send_keys("Welcome to selenium")
    input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
    act=ActionChains(driver)
    act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    act.send_keys(Keys.TAB).perform()
    act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    time.sleep(5)

