from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time


class WelcomeUserPage(BasePage):

    def __init__(self, driver):
        super(WelcomeUserPage, self).__init__(driver)
        # self.welcome_signin_page=(By.XPATH,"//h1[normalize-space()='Welcome, Please Sign In!'])[1]")
        self.checkout_guest_button=(By.XPATH,"//button[normalize-space()='Checkout as Guest']")
        self.billing_page_checkout_title=(By.CSS_SELECTOR,"div[class='page-title'] h1")

    def checkout_as_guest(self): 
        self.driver.find_element(*self.checkout_guest_button).click() 
        return self.driver.find_element(*self.billing_page_checkout_title).text
