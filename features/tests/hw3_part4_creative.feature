# Created by laurautarbayeva at 2/21/23
Feature: Adding a vase to the cart
  # Enter feature description here

  Scenario: Making sure that a user can add a vase to the cart
    Given Open Amazon page
    When Search for Glass Vase product
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)



#  Create your own test case to add any product you want into the cart,
#  and make sure it’s there (check for the number of items in the cart OR open the
#  cart and verify it’s there, up to you!)