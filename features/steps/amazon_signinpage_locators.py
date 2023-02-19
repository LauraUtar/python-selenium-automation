from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "/Users/laurautarbayeva/Desktop/Careerist_New/python-selenium-automation")

# Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By. XPATH, '//input[@class="a-button-input"]')


# Need help link


# Forgot your password link


# Other issues with Sign-In link


# Create your Amazon account button


# *Conditions of use link


# *Privacy Notice link
