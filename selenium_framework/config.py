from selenium import webdriver


class DriverSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if DriverSingleton._instance is None:
            options = webdriver.ChromeOptions()
            options.page_load_strategy = 'eager'
            DriverSingleton._instance = webdriver.Chrome(options=options)
            DriverSingleton._instance.maximize_window()
            DriverSingleton._instance.implicitly_wait(10)
        return DriverSingleton._instance

    @staticmethod
    def quit():
        if DriverSingleton._instance:
            DriverSingleton._instance.quit()
            DriverSingleton._instance = None


driver_singleton = DriverSingleton().get_instance()
