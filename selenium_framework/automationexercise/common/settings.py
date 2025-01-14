from faker import Faker
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


fake = Faker()
load_dotenv()


logging_level = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


class Settings(BaseSettings):
    user_name: str = fake.first_name()
    user_email: str = fake.company_email()
    password: str = fake.password()
    existing_email: str = ''
    logging_level: str = 'DEBUG'


settings = Settings()
settings.logging_level = settings.logging_level.upper()
if settings.logging_level not in logging_level:
    settings.logging_level = 'DEBUG'
