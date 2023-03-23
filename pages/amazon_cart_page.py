from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from datetime import datetime


class Amazon_Cart(Page):
    CART_ICON = (By.ID, "nav-cart-count")
    EMPTY_CART = (By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]')
    CART = (By.XPATH, "//input[@class='a-button-input']")


    def verify_cart_is_empty(self):
        actual_result = self.driver.find_element(*self.EMPTY_CART).text
        expected_result = 'Your Amazon Cart is empty'
        assert expected_result == actual_result, f'Expected {expected_result} does not match {actual_result}'

