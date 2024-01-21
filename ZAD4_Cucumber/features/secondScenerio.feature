Feature: WKDZIK Dropdown Menu

  Scenario Outline: Verify dropdown menu and clicking specific WKDZIK pannel on <browser> browser
    Given I open the website "https://wkdzik.pl/" using "<browser>" browser
    When I click on accept cookies button
    And I hover specific dropdown menu
    And I click specific product pannel
    Then I should be on the correct subpage

    Examples:
      | browser |
      | Chrome  |
      | Edge |