import traceback

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import shared
from selenium_framework.automationexercise.common.logger import logger
from selenium_framework.automationexercise.common.settings import settings


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture
def headless(request):
    return request.config.getoption("--headless")


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_type, headless):
    if (browser_type or settings.browser) == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,  # Disable password manager
            "profile.password_manager_enabled": False,  # Disable saving passwords
            "autofill.profile_enabled": False  # Disable autofill
        })
        options.page_load_strategy = 'eager'
        if headless or settings.headless:
            options.add_argument("-headless")
        shared.driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        if headless or settings.headless:
            options.add_argument("-headless")
        shared.driver = webdriver.Firefox(options=options)

    if headless or settings.headless:
        options.add_argument("-headless")

    shared.driver.maximize_window()

    shared.driver.implicitly_wait(10)  # switch to exp implicit wait
    shared.wait = WebDriverWait(shared.driver, settings.explicit_wait)

    shared.driver.get(base_url)

    logger.debug(f'WebDriver initialized: {shared.driver.name}')
    yield shared.driver

    logger.debug('Closing WebDriver')
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

