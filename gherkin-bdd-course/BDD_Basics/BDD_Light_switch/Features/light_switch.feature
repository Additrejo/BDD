Feature: Light switch
  As a user
  I want to turn a light on and off
  So that I can control the lighting in a room

  Scenario: Light is off by default
    Given a new light switch
    Then the light should be off

  Scenario: Turn the light on
    Given a new light switch
    When I toggle the switch
    Then the light should be on

  Scenario: Turn the light off again
    Given a new light switch
    When I toggle the switch
    And I toggle the switch
    Then the light should be off