import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_framework.automationexercise.common.locators import base_url

from selenium_framework.automationexercise.common import shared
from selenium_framework.automationexercise.common.logger import logger


@pytest.fixture(scope='function', autouse=True)
def browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,  # Disable password manager
        "profile.password_manager_enabled": False,  # Disable saving passwords
        "autofill.profile_enabled": False  # Disable autofill
    })
    shared.driver = webdriver.Chrome(options=options)
    shared.driver.maximize_window()

    # shared.driver.implicitly_wait(10)  # switch to exp implicit wait
    shared.wait = WebDriverWait(shared.driver, 10)

    shared.driver.get(base_url)

    logger.warning('WebDriver initialized')
    yield shared.driver

    shared.driver.quit()


def pytest_runtest_call(item):
    logger.warning(f"{item.cls.__name__}::{item.function.__name__}")
