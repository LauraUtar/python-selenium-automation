# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Watches into search field
    And Click on search icon
    Then Product results for Watches are shown


  Scenario: User can see that every product on Amazon search has a product name and a product image
    Given Open Amazon Search Results page for blouse
    Then Verify that each product has a product name and a product image

