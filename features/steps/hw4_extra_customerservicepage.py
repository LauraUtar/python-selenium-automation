from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BOXES_ELEMENTS= (By.CSS_SELECTOR, "div.issue-card-container div.fs-match-card")


# A_DELIVERY_ORDER_OR_RETURN= (By.XPATH, "/div[text()='A delivery, order or return']")
# ADDRESS_SECURITY_AND_PRIVACY= (By.XPATH, "//div[text()='Address, security and privacy']")
# EBOOKS_PRIME_VIDEOS_OR_MUSIC= (By.XPATH, "//div[text()='eBooks, Prime Videos or Music']")
# LOGIN_PASSWORD= (By.XPATH, "//div[text()='eBooks, Prime Videos or Music']")
# PRIME= (By.XPATH, "//div[text()='Prime']")
# MEMBERSHIPS_SUBSCRIPTIONS_OR_COMMUNICATIONS= (By.XPATH, "//div[text()= 'Memberships, subscriptions or communications']")
# ACCESSIBILITY= (By.XPATH, "//div[text()='Accessibility']")
# PAYMENT_CHARGES_OR_GIFT_CARDS= (By.XPATH, "//div[text()='Payment, charges or gift cards']")
# KINDLE_FIRE_ALEXA= (By.XPATH, "//div[text()='Kindle, Fire, Alexa or Other Amazon Devices']")
# SOMETHING_ELSE= (By.XPATH, "//div[text()= 'Something else']")


@given('Open Amazon Customer Service Page')
def open_amazon_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@then('Verify these UI elements are present of the page')
def verify_these_UI_elements_are_present_of_the_page(context):
    number_of_elements = len(context.driver.find_elements(*BOXES_ELEMENTS))
    expected_number_of_elements = 10
    assert number_of_elements == expected_number_of_elements

    # context.driver.find_elements(*A_DELIVERY_ORDER_OR_RETURN)
    # context.driver.find_elements(*ADDRESS_SECURITY_AND_PRIVACY)
    # context.driver.find_elements(*EBOOKS_PRIME_VIDEOS_OR_MUSIC)
    # context.driver.find_elements(*LOGIN_PASSWORD)
    # context.driver.find_elements(*PRIME)
    # context.driver.find_elements(*MEMBERSHIPS_SUBSCRIPTIONS_OR_COMMUNICATIONS)
    # context.driver.find_elements(*ACCESSIBILITY)
    # context.driver.find_elements(*PAYMENT_CHARGES_OR_GIFT_CARDS)
    # context.driver.find_elements(*KINDLE_FIRE_ALEXA)
    # context.driver.find_elements(*SOMETHING_ELSE)
