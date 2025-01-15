from typing import Literal

from faker import Faker
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


fake = Faker()
load_dotenv()

LoggingLevel = Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


class Settings(BaseSettings):
    user_name: str = fake.first_name()
    user_email: str = fake.company_email()
    password: str = fake.password()
    existing_email: str = ''
    logging_level: LoggingLevel = 'DEBUG'
    explicit_wait: int = 5
    headless: bool = False
    browser: str = 'chrome'


settings = Settings()
