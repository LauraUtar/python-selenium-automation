# Created by laurautarbayeva at 2/20/23
Feature: Test Scenario for Returns and Orders  # Update a test case to verify that logged out user sees Sign In when clicking on Returns and Orders to use Behave (BDD) (test case from Ex 2 of HW2)
#create page object modal
  Scenario: User can see Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click Returns and Orders
    Then Sign in page opened