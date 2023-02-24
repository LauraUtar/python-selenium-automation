from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


RETURN_AND_ORDERS = (By.ID, 'nav-orders')
SIGN_IN = (By.XPATH, "//h1")
CART_ICON = (By.ID, "nav-cart-count")
EMPTY_CART = (By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]')
SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
SEARCH_BTN = (By.ID, "nav-search-submit-button")
FIRST_PRODUCT = (By.XPATH, '//div[@class="a-section aok-relative s-image-square-aspect"]/div/img[contains(@data-image-index, "1")]')
ADD_TO_CART = (By.ID, "add-to-cart-button")
CART = (By.XPATH, "//input[@class='a-button-input']")
ALL_PRODUCTS = (By.XPATH, "//div[@class='s-main-slot s-result-list s-search-results sg-row']/div/div/div/div/div/div/span/a")
SUCCESS_MSG = (By.XPATH, "//div[@id='NATC_SMART_WAGON_CONF_MSG_SUCCESS']/span")
CART_QUANTITY = (By.XPATH, "//li[@class='sw-product-variation']/span/span[2]")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('click Returns and Orders')
def click_returns_and_orders(context):
    context.driver.find_element(*RETURN_AND_ORDERS).click()

@then('Sign in page opened')
def sign_in_page_opened(context):
    actual_result = context.driver.find_element(*SIGN_IN).text
    expected_result = 'Sign in'
    assert expected_result == actual_result, f'Expected {expected_result} does not match {actual_result}'
    print('Test case passed')

@when('Click on the cart icon')
def click_on_the_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()

@then('Cart is empty')
def cart_is_empty(context):
    actual_result = context.driver.find_element(*EMPTY_CART).text
    expected_result = 'Your Amazon Cart is empty'
    assert expected_result == actual_result, f'Expected {expected_result} does not match {actual_result}'
    print('Test case passed')

@then('Add the first item from the list to cart')
def add_the_first_item_from_the_list_to_cart(context):
    # context.driver.find_element(*GLASS_VASE)
    pass

@when('Search for {search_word} product')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(1)


@step("Click on the first product")
def click_on_the_first_product(context):
    all_products = context.driver.find_elements(*ALL_PRODUCTS)
    all_products[0].click()

#
# @step("Store product name")
# def store_product_name(context):



@step("Click on Add to cart button")
def click_on_add_to_cart_button(context):
    sleep(3)
    context.driver.find_element(*ADD_TO_CART).click()


@step("Open cart page")
def step_impl(context):
    context.driver.find_element(*CART).click()


@then('Verify cart has {quantity} item(s)')
def step_impl(context, quantity):
    expected_text = "Added to Cart"
    actual_text = context.driver.find_element(*SUCCESS_MSG).text
    assert expected_text == actual_text, f"Expected text not found but found {actual_text}"
    actual_quantity = context.driver.find_elements(*CART_QUANTITY)[0].text
    actual_quantity = quantity.replace(" ", "")
    assert quantity ==actual_quantity, f"Expected {quantity} quantity but found {actual_quantity} quantity"






@step("Verify cart has correct product")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And Verify cart has correct product')