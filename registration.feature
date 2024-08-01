Feature: User Registration

  Scenario: Successful registration
    Given I am on the registration page
    When I fill in the registration form with valid data
    And I submit the form
    Then I should see a confirmation of registration
