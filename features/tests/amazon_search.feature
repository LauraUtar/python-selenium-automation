# Created by laurautarbayeva at 4/2/23
Feature: Tests for Amazon search

#  Scenario Outline: User can search for a product
#    Given Open Amazon
#    When Search for <search_word>
#    Then Verify search results are shown for <expected_result>
#    Examples:
#    |search_word    |expected_result    |
#    |coffee         |"coffee"           |
#    |table          |"table"            |
#    |dress          |"dress"            |



  Scenario: User can see language options
     Given Open Amazon
     When Hover over language options
     Then Verify Spanish option present


    #HW8
  Scenario Outline: User can select and search in a department
      Given Open Amazon
      When Select department by <dept_alias>
      And Search for <search_query>
      Then Verify <selected_dept> department is selected
      Examples:
      |dept_alias           |search_query      |selected_dept        |
      |stripbooks           |Faust             |books                |
      |audible              |Alice in          |audible              |
      |wholefoods           |grapes            |wholefoods           |
      |beauty               |mascara           |beauty               |
      |mi                   |piano keyboard    |mi                   |
      |luxury-beauty        |Bags              |luxury-beauty        |



  Scenario: User can see that every product on Amazon search has a product name and a product image
    Given Open Amazon Search Results page for blouse
    Then Verify that each product has a product name and a product image

