from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name ul li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name div.a-row span")
BLOUSE_PRODUCTS = (By.CSS_SELECTOR, ".a-section.aok-relative.s-image-tall-aspect")
BLOUSE_NAME = (By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]')

@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"


@given ('Open Amazon page product {product_id} page')
def Open_Amazon_page_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@then ('Verify that user can click through colors')
def Verify_that_user_can_click_through_colors(context):
    context.driver.find_element(*COLOR_OPTIONS).click() # click on 1

    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All colors:', all_color_options)
    expected_colors = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage']

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('Current color', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

    # Extra task for HW5 I chose a blouse as a product not coffee
@given('Open Amazon Search Results page for blouse')
def Open_Amazon_Search_Results_page(context):
    context.driver.get(
        'https://www.amazon.com/s?k=blouse&crid=OVJULRY4XFMK&sprefix=blouse%2Caps%2C138&ref=nb_sb_ss_ts-doa-p_3_6')

@then('Verify that each product has a product name and a product image')
def Verify_that_each_product_has_a_product_name_and_a_product_image(context):
    # blouse_elements = context.driver.find_elements(*BLOUSE_NAME)
    # print(len(blouse_elements))
    # for blouse_element in blouse_elements:
    #     if len(blouse_element.text) == 0:
    #         print("no name")
    #         continue
    #     print(blouse_element.text)
    #     assert 'blouse' in blouse_element.text.lower(), f'Expected Blouse to be in element, got {blouse_element.text}'
    #
    # number_of_pictures = len(context.driver.find_elements(*BLOUSE_PRODUCTS))
    # assert number_of_pictures == len(
    #     blouse_elements), f'Expected Blouse pictures {str(len(blouse_elements))}, got {str(number_of_pictures)}'

    blouse_elements = context.driver.find_elements(*BLOUSE_NAME)[:5]
    for blouse_element in blouse_elements:
        assert blouse_element.is_displayed(), "The element doesn't contain a title"

    pictures = context.driver.find_elements(*BLOUSE_PRODUCTS)[:5]
    for picture in pictures:
        assert picture.is_displayed(), "The element doesn't contain a picture"