from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='./chromedriver')


driver.get('https://www.amazon.com')
driver.find_element(By.ID, "nav-orders").click()

expected_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
actual_result = driver.find_element(By.XPATH, "//h1").text
assert expected_result == actual_result, f'Expected {expected_result} does not match {actual_result}'
print('Test case passed')
driver.quit()