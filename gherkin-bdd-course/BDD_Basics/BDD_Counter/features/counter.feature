Feature: Counter
  As a user
  I want to count events
  So that I can keep track of how many times something happened

  Scenario: Counter starts at zero
    Given a new counter
    Then the counter value should be 0

  Scenario: Increment the counter once
    Given a new counter
    When I increment the counter
    Then the counter value should be 1

  Scenario: Increment the counter three times
    Given a new counter
    When I increment the counter
    And I increment the counter
    And I increment the counter
    Then the counter value should be 3

  Scenario: Reset the counter
    Given a new counter
    When I increment the counter
    And I reset the counter
    Then the counter value should be 0