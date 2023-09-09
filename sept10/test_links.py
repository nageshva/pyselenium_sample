import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_link():
    driver = webdriver.Chrome()
    mywait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("http://www.deadlinkcity.com/")
    all_links=driver.find_elements(By.TAG_NAME,"a")
    count=0

    for link in all_links:
        url=link.get_attribute('href')
        res=requests.head(url)
        if res.status_code>=400:
            print(url,"is broken")
            count+=1



