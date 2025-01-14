# ui_automation_example
Example of UI testing via Python automation

**Конфигурация проекта**

Скопировать проект, перейти в папку с проектом.
Создать виртуальное окружение командой:

`python -m venv venv`

Активировать окружение, выполнив команду:

`.\venv\Scripts\activate`

**Установить зависимости**

_pip_

`pip install -r requirements.txt`


**Запуск тестов**

Все тесты: `pytest .`

**Тестовый стенд - `https://automationexercise.com/`**

Тесты с использованием фреймворка Selenium: `pytest .\selenium_framework\tests\`

test_open_page() - проверка открытия главной страницы по url заголовка

test_register_new_user() - проверка регистрации нового пользователя с заполнением данных аккаунта и проверки
сообщения об успешном создании. После создания - аккаунт удаляется через кнопку через кнопку меню.

test_register_existing_user() - проверка попытки регистрации нового пользователя, используя уже существующий 
в базе email. Проверяется сообщение об ошибке.
