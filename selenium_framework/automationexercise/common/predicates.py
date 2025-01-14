from selenium.webdriver.common.by import By

from selenium_framework.automationexercise.common import shared as s
from selenium.webdriver.support import expected_conditions as EC


def is_not_displayed(locator: tuple[str, str]):
    return s.wait.until(EC.invisibility_of_element_located(*locator))


def is_displayed(locator: tuple[str, str]):
    return s.wait.until(EC.visibility_of_element_located(locator))
