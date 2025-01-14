import traceback

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_framework.automationexercise.common.locators import base_url

from selenium_framework.automationexercise.common import shared
from selenium_framework.automationexercise.common.logger import logger
from selenium_framework.automationexercise.common.settings import settings


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
    shared.wait = WebDriverWait(shared.driver, settings.explicit_wait)

    shared.driver.get(base_url)

    logger.debug('WebDriver initialized')
    yield shared.driver

    logger.debug('Close WebDriver')
    shared.driver.quit()


def pytest_runtest_call(item):
    logger.warning(f"{item.cls.__name__}::{item.function.__name__}: {item.function.__doc__.replace('/n', '').strip()}")


# This hook runs after each test is executed
def pytest_runtest_makereport(item, call):
    if call.when == 'call':  # Only log the results after the test call
        if call.excinfo is None:  # Test passed
            logger.warning(f"Test PASSED: {item.name}")
        else:  # Test failed
            logger.error(f"Test FAILED: {item.name} - {call.excinfo.value}")

