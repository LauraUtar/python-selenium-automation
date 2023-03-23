from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from datetime import datetime


class Signin(Page):
    SIGN_IN = (By.XPATH, "//h1")

    def sign_in_page_opened(self):
        actual_result = self.driver.find_element(*self.SIGN_IN).text
        expected_result = 'Sign in'
        assert expected_result == actual_result, f'Expected {expected_result} does not match {actual_result}'
