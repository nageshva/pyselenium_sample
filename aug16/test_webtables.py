import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
def test_webtables_01():

    driver=webdriver.Chrome()
    #driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    #Row

    row_elements=driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row_length=len(row_elements)
    print(row_length)
    #Col

    col_elements=driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col_length=len(col_elements)
    print(col_length)

    first_part="//table[contains(@id,'cust')]/tbody/tr["
    second_part="]/td["
    third_part="]"

    # for i in range(2,row_length+1):
    #     for j in range(1,col_length+1):
    #         data=driver.find_element(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr[i]/td[j]")
    #         print(data.text)

    #if i want to find Helen Bennett's country
    for i in range(2,row_length+1):
        for j in range(1,col_length+1):
            dynamic_path=f"{first_part}{i}{second_part}{j}{third_part}"
            data=driver.find_element(By.XPATH,dynamic_path)
            print(data.text)
            # if "Helen Bennett" in data.text:
            #     country_path=f"{dynamic_path}/following-sibling::td"
            #     country_text =driver.find_element(By.XPATH,country_path).text
            #     print(f"Helen Bennet is in {country_text}")

# when rows and columns are irregular
#     row_table =driver.find_elements(By.XPATH,"//table[@summary='Sample Table']/tbody/tr")
#
#     for row in row_table:
#         col= row.find_elements(By.TAG_NAME,"td") # //table[@summary='Sample Table']/tbody/tr/td
#         for e in col:
#             print(e.text)





