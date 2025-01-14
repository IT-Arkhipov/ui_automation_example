import inspect

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
        logger.info(f'{__name__.split(".")[-1]}::{inspect.currentframe().f_code.co_name}: ' + eval(
            f'self.{inspect.currentframe().f_code.co_name}.__doc__').replace('/n', '').strip())

        get(self.url)
        url_to_be(self.url)

    def click_login_button(self):
        """
        Клик по кнопке "Sign Up / Login"
        """
        logger.info(f'{__name__.split(".")[-1]}::{inspect.currentframe().f_code.co_name}: ' + eval(
            f'self.{inspect.currentframe().f_code.co_name}.__doc__').replace('/n', '').strip())

        element((By.XPATH, self.signup_login)).click()


main_page = MainPage()
