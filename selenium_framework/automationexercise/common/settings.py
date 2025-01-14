from faker import Faker
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


fake = Faker()
load_dotenv()


class Settings(BaseSettings):
    user_name: str = fake.first_name()
    user_email: str = fake.company_email()
    password: str = fake.password()
    logging_level: str = 'INFO'


settings = Settings()
