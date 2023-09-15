import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_MouseAction():
    driver=webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://testautomationpractice.blogspot.com/")
#double click action
    # filed1=driver.find_element(By.XPATH,"//input[@id='field1']")
    # filed1.clear()
    # filed1.send_keys("Welcome")
    # copytext=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
    # act = ActionChains(driver)
    # act.move_to_element(copytext).double_click(copytext).perform()
#drag and drop
    # source=driver.find_element(By.XPATH,"//p[normalize-space()='Drag me to my target']")
    # target=driver.find_element(By.XPATH,"//div[@id='droppable']")
    #
    # print("Before drag...")
    # print(source.location, target.location)
    # act=ActionChains(driver)
    # act.move_to_element(source).perform()
    # #act.drag_and_drop(source,target).perform()
    # act.drag_and_drop_by_offset(source,100,0).perform()
    # time.sleep(10)
    # print("after drag....")
    # print(source.location,target.location)


#sliding bar

    # slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
    # act = ActionChains(driver)
    # act.move_to_element(slider).perform()
    # act.drag_and_drop_by_offset(slider,100,10).perform()
    # time.sleep(5)

#Rightclick
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    rightclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
    act = ActionChains(driver)
    act.move_to_element(rightclick).perform()
    act.context_click(rightclick).perform()
    time.sleep(10)

