Feature: Ninja BMI
  In order to increase the ninja survival rate,
  As a ninja commander
  I want my ninjas to know their BMIs so they can work harder

  Scenario: Ninjas know BMI
    Given open App index page
    When user type in weight: 80 and height: 180
    And select the Submit button
    Then BMI is displayed as 24.691358024691358
    When select the Show button
    Then life expectancy is displayed as 75.30864197530865
