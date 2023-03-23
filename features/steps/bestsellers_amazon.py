from selenium.webdriver.common.by import By
from behave import given, when, then

# BEST_SELLERS_BLOCK = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")
BEST_SELLERS_BLOCK = (By. CSS_SELECTOR, '#zg_header a')
LINK_NAMES = {"Best Sellers",
               "New Releases",
               "Movers & Shakers",
               "Most Wished For",
               "Gift Ideas"}
HEADER = (By. CSS_SELECTOR, '#zg_banner_text')
# HEADER = (By.XPATH, '//div[@class="_p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR"]')


@given('Open Bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_result} links')
def verify_there_are_5_links(context, expected_result):
    actual_result = context.driver.find_elements(*BEST_SELLERS_BLOCK)
    assert expected_result == str(len(actual_result)), f'Expected {expected_result} but got {actual_result}'


@then("User can click on each top link and verify that correct page opens")
def step_impl(context):
    expected_link_names = context.driver.find_elements(*BEST_SELLERS_BLOCK)
    print(expected_link_names)

    for i in range(len(expected_link_names)): # for x from 0 to 4
        link_to_click = context.driver.find_elements(*BEST_SELLERS_BLOCK)[i]
        link_text = link_to_click.text
        print(link_text)
        link_to_click.click()
        header_text = context.driver.find_element(*HEADER).text
        print(header_text)
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'


