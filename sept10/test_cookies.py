import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_cookie():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    cookies=driver.get_cookies() # here cookies  are in the form of dictionary object contains key and value pairs
    print('before adding cookie.......')
    print(len(cookies))

# lets see the deatils of cookie info

    # for c in cookies:
    #     print(c.get('value')) # here we are extracting cookie names

# add new cookie to browser

    driver.add_cookie({'name':'MyCookie','value':'0X5789fyt'})
    cookies = driver.get_cookies()
    print('after adding cookie.......')
    print(len(cookies))
    # for c in cookies:
    #   print(c)
# delete new cookie to browser
#
#     driver.delete_cookie('Mycookie')
#     cookies = driver.get_cookies()
#     print('after deleting cookie.......')
#     print(len(cookies))


    driver.delete_all_cookies()
    cookies = driver.get_cookies()
    print('after deleting cookie.......')
    print(len(cookies))

