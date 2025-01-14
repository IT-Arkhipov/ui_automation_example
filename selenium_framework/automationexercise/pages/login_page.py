from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from faker import Faker

from selenium_framework.automationexercise.common import shared as s
from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common import predicates

from selenium_framework.automationexercise.settings import settings

fake = Faker()


class LoginPage:
    email_exists_message = "Email Address already exist!"
    url = urljoin(base_url, 'login')

    signup_form = '//form[@action="/signup"]'
    input_name = '//input[@type="text"]'
    input_email = '//input[@type="email"]'
    submit_btn = '//button[@type="submit"]'

    def check_page_url(self):
        assert s.driver.current_url == self.url

    def fill_signup_form_new_user(self):
        """
        Заполнение формы регистрации новыми данными пользователя
        """
        assert predicates.is_displayed(self.signup_form)
        name_field = s.driver.find_element(By.XPATH, self.signup_form + self.input_name)
        email_field = s.driver.find_element(By.XPATH, self.signup_form + self.input_email)
        submit = s.driver.find_element(By.XPATH, self.signup_form + self.submit_btn)
        name_field.send_keys(settings.user_name)
        email_field.send_keys(settings.user_email)
        submit.click()

    def fill_signup_form_existing_email(self, existing_email: str):
        """
        Заполнение формы регистрации с существующим email
        """
        assert predicates.is_displayed(self.signup_form)
        name_field = s.driver.find_element(By.XPATH, self.signup_form + self.input_name)
        email_field = s.driver.find_element(By.XPATH, self.signup_form + self.input_email)
        submit = s.driver.find_element(By.XPATH, self.signup_form + self.submit_btn)
        name_field.send_keys(settings.user_name)
        email_field.send_keys(existing_email)
        submit.click()
        signup_form = s.driver.find_element(By.XPATH, self.signup_form)
        # проверка наличия сообщения об ошибке
        assert self.email_exists_message in signup_form.text


login_page = LoginPage()
