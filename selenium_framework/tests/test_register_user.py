from selenium_framework.automationexercise.pages.import_pages import *


class TestRegisterUser:
    """
    Тестирование регистрации нового пользователя
    """

    def test_open_page(self):
        """
        Проверка открытия главной страницы
        """
        mp = main_page

        mp.open()

    def test_register_new_user(self):
        """
        Проверка регистрации нового пользователя с уникальным email
        """
        mp = main_page
        lp = login_page
        ap = account_register_page

        mp.click_login_button()

        lp.check_page_url()
        lp.fill_signup_form_new_user()

        ap.check_page_url()
        ap.fill_account_info()
        ap.verify_account_created()
        ap.delete_account()
        ap.verify_account_deleted()

    def test_register_existing_user(self):
        """
        Проверка попытки регистрации пользователя с уже существующим email
        """
        mp = main_page
        lp = login_page

        existing_email = "test@test.com"

        mp.click_login_button()

        lp.check_page_url()
        lp.fill_signup_form_existing_email(existing_email)
