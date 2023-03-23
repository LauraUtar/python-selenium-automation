from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.ID, "nav-cart-count")
    RETURN_AND_ORDERS = (By.ID, 'nav-orders')

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_return_and_orders(self):
        self.click(*self.RETURN_AND_ORDERS)
