import time

from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")
WINDOW_ORIGINAL=""
PRIVACY_NOTICE= (By.LINK_TEXT, "Privacy Notice")
# AMAZON_PRIVACY = (By.XPATH, "//div[@class='help-content']/h1")
AMAZON_PRIVACY= (By.CSS_SELECTOR, ".help-service-content h1")


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')


@when('Store original windows')
def store_original_windows(context):
    context.driver.window_original = context.driver.current_window_handle



@when('Click on Amazon Privacy Notice link')
def click_on_Amazon_Privacy_Notice_link(context):
    context.driver.find_element(By.LINK_TEXT, "Privacy Notice").click()



@when('Switch to the newly opened window')
def switch_to_the_newly_opened_window(context):
    window_new = context.driver.window_handles[1]
    context.driver.switch_to.window(window_new)



@then('Verify Amazon Privacy Notice page is opened')
def verify_Amazon_Privacy_Notice_page_is_opened(context):
    expected_text = "Amazon.com Privacy Notice"
    actual_text = context.driver.find_element(*AMAZON_PRIVACY).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


@then('User can close new window and switch back to original')
def user_can_close_new_window_and_switch_back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_original)
    # time.sleep(2)