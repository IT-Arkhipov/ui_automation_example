from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import shared as s


# didn't use yet
class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get(base_url)

    @staticmethod
    def element(locator) -> WebElement:
        def find_element(driver: WebDriver) -> WebElement:
            return driver.find_element(*locator)
        return find_element(s.driver)


browser = Browser()


