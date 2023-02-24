from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/")

# Find the most optimal locators for Create Account (Registration) page elements:

# Amazon Logo:
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

# Create Account:
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')

# Your name Field:
driver.find_element(By.ID, 'ap_customer_name')

# Email Field:
driver.find_element(By.ID, 'ap_email')

# Password Field:
driver.find_element(By. ID, 'ap_password')

# Re-Enter Password Field:
driver.find_element(By. ID, 'ap_password_check')

# Continue Button (there was no 'Create Amazon Account' button on my end just 'Continue' one):
driver.find_element(By. ID, 'continue')

# Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use?')]")

# Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice?')]")
