from selenium import webdriver

from selenium_framework.automationexercise.common.locators import base_url


# didn't use yet
class Browser:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get(base_url)


browser = Browser()
