from selenium.webdriver.common.by import By

from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import shared as s


class MainPage:
    url = base_url

    shop_menu = '//*[contains(@class, "shop-menu")]'
    products = '//*[@href="/products"]'
    cart = '//*[@href="/view_cart"]'
    signup_login = '//*[@href="/login"]'

    def open(self):
        s.driver.get(self.url)
        assert s.driver.current_url == self.url

    def click_login_button(self):
        s.driver.find_element(By.XPATH, self.signup_login).click()


main_page = MainPage()
