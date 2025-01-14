import inspect

from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from faker import Faker

from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import predicates
from selenium_framework.automationexercise.common.commands import *
from selenium_framework.automationexercise.common.settings import settings

fake = Faker()


class LoginPage:
    email_exists_message = "Email Address already exist!"
    url = urljoin(base_url, 'login')

    signup_form = '//form[@action="/signup"]'
    input_name = '//input[@type="text"]'
    input_email = '//input[@type="email"]'
    submit_btn = '//button[@type="submit"]'

    def check_page_url(self):
        """
        Проверка текущего url страницы
        """
        logger.info(f'{__name__.split(".")[-1]}::{inspect.currentframe().f_code.co_name}: ' + eval(
            f'self.{inspect.currentframe().f_code.co_name}.__doc__').replace('/n', '').strip())

        assert s.driver.current_url == self.url

    def fill_signup_form_new_user(self):
        """
        Заполнение формы регистрации новыми данными пользователя
        """
        logger.info(f'{__name__.split(".")[-1]}::{inspect.currentframe().f_code.co_name}: ' + eval(
            f'self.{inspect.currentframe().f_code.co_name}.__doc__').replace('/n', '').strip())

        assert predicates.is_displayed((By.XPATH, self.signup_form))
        name_field = element((By.XPATH, self.signup_form + self.input_name))
        email_field = element((By.XPATH, self.signup_form + self.input_email))
        submit = element((By.XPATH, self.signup_form + self.submit_btn))
        name_field.send_keys(settings.user_name)
        email_field.send_keys(settings.user_email)
        submit.click()

    def fill_signup_form_existing_email(self, existing_email: str):
        """
        Заполнение формы регистрации имеющимся в базе email
        """
        logger.info(f'{__name__.split(".")[-1]}::{inspect.currentframe().f_code.co_name}: ' + eval(
            f'self.{inspect.currentframe().f_code.co_name}.__doc__').replace('/n', '').strip())

        assert predicates.is_displayed((By.XPATH, self.signup_form))
        name_field = element((By.XPATH, self.signup_form + self.input_name))
        email_field = element((By.XPATH, self.signup_form + self.input_email))
        submit = element((By.XPATH, self.signup_form + self.submit_btn))
        name_field.send_keys(settings.user_name)
        email_field.send_keys(existing_email)
        submit.click()
        signup_form = element((By.XPATH, self.signup_form))
        # проверка наличия сообщения об ошибке
        assert self.email_exists_message in signup_form.text


login_page = LoginPage()
