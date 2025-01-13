import pytest
from selenium import webdriver

from selenium_framework.automationexercise.resources.locators import base_url
from selenium_framework.config import driver_singleton as driver


@pytest.fixture(scope='session', autouse=True)
def browser():
    # options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.implicitly_wait(10)

    driver.get(base_url)

    yield driver  # Yield the driver for use in tests

    driver.quit()  # Quit the driver after all tests are done
