from selenium.webdriver.remote.webelement import WebElement

from selenium_framework.automationexercise.common import shared as s
from selenium.webdriver.support import expected_conditions as EC


def get(url: str):
    s.driver.get(url)


def url_to_be(url: str):
    s.wait.until(EC.url_to_be(url))


def element(locator: tuple) -> WebElement:
    return s.wait.until(EC.visibility_of(s.driver.find_element(*locator)))


def elements(locator: tuple[str, str]) -> list[WebElement]:
    return s.wait.until(EC.presence_of_all_elements_located(locator))
