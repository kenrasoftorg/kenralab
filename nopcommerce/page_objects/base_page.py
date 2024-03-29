class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        self.driver.find_element(*locator)
