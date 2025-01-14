from selenium.webdriver.common.by import By

from selenium_framework.automationexercise.common import shared as s


def is_present(locator: str):
    return len(s.driver.find_elements(By.XPATH, locator)) > 0


def is_absent(locator: str):
    return not is_present(locator)


def is_displayed(locator: str):
    return s.driver.find_element(By.XPATH, locator).is_displayed()
