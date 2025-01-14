from selenium.webdriver.common.by import By


from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common.commands import *


class MainPage:
    url = base_url

    # MainPage locators
    shop_menu = '//*[contains(@class, "shop-menu")]'
    products = '//*[@href="/products"]'
    cart = '//*[@href="/view_cart"]'
    signup_login = '//*[@href="/login"]'

    def open(self):
        """
        Открытие с проверкой на соответствие url страницы
        """
        get(self.url)
        url_to_be(self.url)

    def click_login_button(self):
        element((By.XPATH, self.signup_login)).click()


main_page = MainPage()
