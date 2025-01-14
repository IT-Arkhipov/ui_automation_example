import pytest
from selenium import webdriver

from selenium_framework.automationexercise.common.locators import base_url

from selenium_framework.automationexercise.common import shared


@pytest.fixture(scope='function', autouse=True)
def browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'

    shared.driver = webdriver.Chrome(options=options)
    shared.driver.maximize_window()
    shared.driver.implicitly_wait(10)

    shared.driver.get(base_url)

    yield shared.driver  # Yield the driver for use in tests

    shared.driver.quit()  # Quit the driver after all tests are done
