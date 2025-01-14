from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import shared as s


class MainPage:
    url = base_url

    def open(self):
        s.driver.get(self.url)
        assert s.driver.current_url == self.url


main_page = MainPage()
