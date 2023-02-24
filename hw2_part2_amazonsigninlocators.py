from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/")

# Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo"]')

# Email field
driver.find_element(By.ID, 'ap_email')

# Continue button
driver.find_element(By. XPATH, '//input[@class="a-button-input"]')

# Need help link
driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')

# *Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use?')]")

# *Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice?')]")