from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, 'td.navFooterDescItem a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")


@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


# @when('Search for {keyword}')
# def search_amazon(context, keyword):
#     # context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
#     # context.driver.find_element(*SEARCH_BTN).click()
#     context.app.header.search_amazon(keyword)


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department by {alias}')
def select_dept(context, alias):
    context.app.header.select_dept(alias)


# @when('Search for {search_query}')
# def search_query(context, search_query):
#     context.app.header.search_query(search_query)


@then('Verify hamburger menu present')
def verify_ham_menu(context):
    #context.driver.find_element(*HAM_MENU_ICON)
    context.app.main_page.verify_hamburger_icon()


@then('Verify {expected_amount} Links present')
def verify_footer_links_amount(context, expected_amount):
    #expected_amount = int(expected_amount)
    #links_amount = len(context.driver.find_elements(*FOOTER_LINKS))  # [Webelement1, Webelement2,..]

    #assert len(links_amount) == expected_amount, f'Expected {expected_amount} links, but got {len(links_amount)}'
    context.app.main_page.verify_footer_links(expected_amount)

@then('Verify that SignIn popup shown')
def verify_signin_popup(context):
    context.app.main_page.verify_signin_popup_shown()

@then('Verify that SignIn btn is clickable')
def verify_signin_popup_btn_is_clickable(context):
    context.app.main_page.verify_signin_popup_btn_is_clickable()

@then('Verify that SignIn popup disappears')
def verify_signin_popup_btn_disappears(context):
    context.app.main_page.verify_signin_popup_disappears()

@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()

@then('Verify {selected_dept} department is selected')
def verify_department(context, selected_dept):
    context.app.header.verify_department(selected_dept)