from selenium.webdriver.common.by import By

from selenium_framework.config import driver_singleton as driver


def is_present(locator: str):
    return len(driver.find_elements(By.XPATH, locator)) > 0


def is_absent(locator: str):
    return not is_present(locator)
