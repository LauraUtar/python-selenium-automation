import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, "[href='#switch-lang=es_US']")
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    DEPARTMENT_SUB_NAV = (By.CSS_SELECTOR, "[data-category='{SUBSTRING}']")
    NEW_ARRIVALS = (By.CSS_SELECTOR, 'a[href*="/New-Arrivals/b/?"] span.nav-a-content')
    DEALS = (By.XPATH, "//*[contains(@id, 'nav-flyout-aj:')]/div[2]/div/div[1]")
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

    def get_dept_sub_nav_locator(self, department):
        return [self.DEPARTMENT_SUB_NAV[0], self.DEPARTMENT_SUB_NAV[1].replace('{SUBSTRING}', department)]

    def verify_department(self, department):
        department_locator = self.get_dept_sub_nav_locator(department)
        #self.wait_for_element_appear(*department_locator)

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.FLAG)
        actions.move_to_element(flag)
        actions.perform()

    def select_dept(self, alias):
        time.sleep(3)
        department_select = self.find_element(*self.DEPARTMENT_SELECT)
        select = Select(department_select)
        select.select_by_value(f'search-alias={alias}')



    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    # @given('Opens https://www.amazon.com/gp/product/B074TBCSC8 (or any other product from the closing category)')
    # def open_amazon_product(context):
    #     context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')


    def hovers_over_new_arrivals(self):
        actions = ActionChains(self.driver)
        flag = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(flag)
        actions.perform()


    def user_sees_deals(self):
        return self.wait_for_element_appear(*self.DEALS)

    def verify_search_results(self, expected_result):
        self.verify_text(expected_result, *self.SEARCH_RESULT_TEXT)



