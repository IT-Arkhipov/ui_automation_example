from selenium_framework.automationexercise.resources.locators import base_url

from selenium_framework.config import driver_singleton as driver


class MainPage:
    url = base_url

    def open(self):
        driver.get(self.url)
        assert driver.current_url == self.url


main_page = MainPage()
