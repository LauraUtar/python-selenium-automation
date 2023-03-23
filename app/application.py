from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.amazon_cart_page import Amazon_Cart
from pages.signin_page import Signin

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.amazon_cart_page = Amazon_Cart(self.driver)
        self.signin_page = Signin(self.driver)