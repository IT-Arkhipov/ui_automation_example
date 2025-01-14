from faker import Faker

fake = Faker()


class Settings:
    user_name: str = fake.first_name()
    user_email: str = fake.company_email()
    password: str = fake.password()


settings = Settings()
