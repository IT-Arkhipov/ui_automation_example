import random
from urllib.parse import urljoin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium_framework.automationexercise.common.locators import base_url
from selenium_framework.automationexercise.common.settings import settings
from selenium_framework.automationexercise.common.commands import *
from faker import Faker

from helpers import util

fake = Faker()


class AccountRegistrationPage:
    signup_url = urljoin(base_url, 'signup')
    account_created_url = urljoin(base_url, 'account_created')
    account_deleted_url = urljoin(base_url, 'delete_account')

    # page locators
    account_info_name = '//input[@id="name"]'
    account_info_email = '//input[@id="email"]'
    indexed_title_radio = lambda self, x: f'//label[@for="id_gender{x}"]'
    account_info_password = '//input[@id="password"]'
    account_info_first_name = '//input[@id="first_name"]'
    account_info_last_name = '//input[@id="last_name"]'
    account_info_company = '//input[@id="company"]'
    account_info_address = '//input[@id="address1"]'
    account_info_state = '//input[@id="state"]'
    account_info_city = '//input[@id="city"]'
    account_info_zipcode = '//input[@id="zipcode"]'
    account_info_mobile_number = '//input[@id="mobile_number"]'

    account_info_checkboxes = '//*[@class="checkbox"]//label'
    create_account_btn = '//button[@data-qa="create-account"]'
    account_creation_success = '//*[@data-qa="account-created"]'
    account_deletion_success = '//*[@data-qa="account-deleted"]'
    continue_btn = '//*[@data-qa="continue-button"]'

    date_of_birth = '//select[@id="days"]'
    month_of_birth = '//select[@id="months"]'
    years_of_birth = '//select[@id="years"]'
    country = '//select[@id="country"]'
    countries_name = '//select[@id="country"]/option'

    delete_account_btn = '//*[@href="/delete_account"]'
    logout_btn = '//*[@href="/logout"]'

    def check_page_url(self):
        assert s.driver.current_url == self.signup_url

    def fill_account_info(self):
        """
        Заполнение данных пользователя
        """
        # проверка введенного имени и email пользователя
        account_name = element((By.XPATH, self.account_info_name))
        assert settings.user_name == account_name.get_attribute('value')
        account_email = element((By.XPATH, self.account_info_email))
        assert settings.user_email == account_email.get_attribute('value')

        title_radio = element((By.XPATH, self.indexed_title_radio(random.randint(1, 2))))
        title_radio.click()

        settings.password = fake.password()
        account_password = element((By.XPATH, self.account_info_password))
        account_password.send_keys(settings.password)

        random_date = util.random_date(start_year=1900, end_year=2021, date_format="%d %B %Y")

        account_date = element((By.XPATH, self.date_of_birth))
        selector = Select(account_date)
        selector.select_by_visible_text(f'{int(random_date.split()[0])}')

        account_month = element((By.XPATH, self.month_of_birth))
        selector = Select(account_month)
        selector.select_by_visible_text(random_date.split()[1])

        account_year = element((By.XPATH, self.years_of_birth))
        selector = Select(account_year)
        selector.select_by_value(random_date.split()[2])

        account_first_name = element((By.XPATH, self.account_info_first_name))
        account_first_name.send_keys(fake.first_name())
        account_last_name = element((By.XPATH, self.account_info_last_name))
        account_last_name.send_keys(fake.last_name())
        account_company = element((By.XPATH, self.account_info_company))
        account_company.send_keys(fake.company())

        countries = elements((By.XPATH, self.countries_name))
        countries_name = [country.text for country in countries]
        account_country = element((By.XPATH, self.country))
        selector = Select(account_country)
        selector.select_by_visible_text(random.choice(countries_name))

        account_address = element((By.XPATH, self.account_info_address))
        account_address.send_keys(fake.address())
        account_state = element((By.XPATH, self.account_info_state))
        account_state.send_keys(fake.state())
        account_city = element((By.XPATH, self.account_info_city))
        account_city.send_keys(fake.city())
        account_zipcode = element((By.XPATH, self.account_info_zipcode))
        account_zipcode.send_keys(fake.postcode())
        account_mobile_number = element((By.XPATH, self.account_info_mobile_number))
        account_mobile_number.send_keys(fake.phone_number())

        account_checkboxes = elements((By.XPATH, self.account_info_checkboxes))
        for checkbox in account_checkboxes:
            checkbox.click()

        create_account_btn = element((By.XPATH, self.create_account_btn))
        create_account_btn.click()

    def verify_account_created(self):
        """
        Проверка адреса страницы и сообщения об успешном создании пользователя
        """
        assert s.driver.current_url == self.account_created_url
        assert 'Account Created!'.lower() in element((By.XPATH, self.account_creation_success)).text.lower()
        element((By.XPATH, self.continue_btn)).click()

    def delete_account(self):
        _delete_account_btn = element((By.XPATH, self.delete_account_btn))
        assert _delete_account_btn.is_displayed()
        _delete_account_btn.click()

    def verify_account_deleted(self):
        """
        Проверка адреса страницы и сообщения об удалении пользователя
        """
        assert s.driver.current_url == self.account_deleted_url
        assert 'Account Deleted!'.lower() in element((By.XPATH, self.account_deletion_success)).text.lower()
        element((By.XPATH, self.continue_btn)).click()


account_register_page = AccountRegistrationPage()
