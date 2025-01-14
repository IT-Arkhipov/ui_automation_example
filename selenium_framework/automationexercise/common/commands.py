from selenium.webdriver.remote.webelement import WebElement

from selenium_framework.automationexercise.common import shared as s
from selenium_framework.automationexercise.common.logger import logger
from selenium.webdriver.support import expected_conditions as EC


def get(url: str):
    logger.info(f"Открытие страницы: {url}")
    s.driver.get(url)


def url_to_be(url: str):
    logger.info(f"Проверка url: {url}")
    s.wait.until(EC.url_to_be(url))


def element(locator: tuple) -> WebElement:
    logger.debug(f"Поиск элемента по селектору: {locator[1]}")
    return s.wait.until(EC.visibility_of(s.driver.find_element(*locator)))


def elements(locator: tuple[str, str]) -> list[WebElement]:
    logger.debug(f"Поиск элементов по селектору: {locator[1]}")
    return s.wait.until(EC.presence_of_all_elements_located(locator))
