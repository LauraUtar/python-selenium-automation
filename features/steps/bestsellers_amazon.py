from selenium.webdriver.common.by import By
from behave import given, when, then

# LINKS = (By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")
#
# @given('Open Bestsellers page')
# def open_prime(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
#
# @then('Verify there are 5 links')
# def verify_5_links(context):
#     links_amount = len(context.driver.find_elements(*LINKS))
#     assert links_amount == 5, f'Expected 5 links, but got {links_amount}'





BEST_SELLERS_BLOCK = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li/div/a")

LINK_NAMES = {"Best Sellers",
               "New Releases",
               "Movers & Shakers",
               "Most Wished For",
               "Gift Ideas"}
HEADER = (By.XPATH, '//div[@class="_p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR"]')


@given('Open Bestsellers page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are {expected_result} links')
def verify_there_are_5_links(context, expected_result):
    actual_result = context.driver.find_elements(*BEST_SELLERS_BLOCK)
    assert expected_result == str(len(actual_result)), f'Expected {expected_result} but got {actual_result}'


