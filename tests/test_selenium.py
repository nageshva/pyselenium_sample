
import pytest
from selenium import webdriver
import logging
@pytest.fixture
def driver():

    driver=webdriver.Chrome()
    yield driver

def test_open_url(driver):

    LOGGER = logging.getLogger(__name__)
    driver.get("https://app.vwo.com/")
    print(driver.title)
    #actual result =expected result
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    assert "Login - VWO" == driver.title
