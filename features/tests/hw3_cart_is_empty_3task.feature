# Created by laurautarbayeva at 2/21/23
Feature: Test Scenario to verify that the cart is empty
 #Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.
  #convert to page object modal
  Scenario: User can see Empty cart when clicking on Cart
    Given Open Amazon page
    When Click on the cart icon
    Then Cart is empty