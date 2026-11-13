Feature: Basic calculator operations
  As a calculator user
  I want to perform basic arithmetic operations
  So that I get correct results

  Scenario: Add two numbers
    Given I have a calculator
    When I add 5 and 3
    Then the result should be 8

  Scenario: Subtract two numbers
    Given I have a calculator
    When I subtract 4 from 10
    Then the result should be 6

  Scenario: Multiply two numbers
    Given I have a calculator
    When I multiply 6 and 7
    Then the result should be 42

  Scenario: Divide two numbers
    Given I have a calculator
    When I divide 20 by 4
    Then the result should be 4

  Scenario: Divide by zero
    Given I have a calculator
    When I divide 10 by 0
    Then I should get a division by zero error