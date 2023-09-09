import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_window():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")
    # search_frame=driver.find_element(By.ID,"Wikipedia1_wikipedia-search-form")
    # driver.switch_to.frame(search_frame)
    input_box=driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("selenium")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(2)

    search_results=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div[@id]//a")

    # count=len(suggestion_list)
    # print(count)
    for item in search_results:
        item.click()
        # driver.back()
        time.sleep(2)

        windowIDs = driver.window_handles
        for winid in windowIDs:
            driver.switch_to.window(winid)
            time.sleep(2)
            print(driver.title)
            time.sleep(5)


