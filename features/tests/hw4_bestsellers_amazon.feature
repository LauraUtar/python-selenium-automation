# Created by laurautarbayeva at 2/26/23
Feature: Test Scenario for Bestsellers page

  Scenario: User can open amazon BestSellers page and see there are 5 links
    Given Open Bestsellers page
    Then Verify there are 5 links
