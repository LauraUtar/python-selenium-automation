from selenium import webdriver
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path="/chromedriver")
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path="/geckodriver")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(driver=context.driver)

    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_search.feature

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
