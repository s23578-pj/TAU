Feature: Login functionality test on Wikipedia page

  Scenario Outline: Validate login functionality in <browser> browser
    Given I open the website "https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna" on browser "<browser>"
    When I click on the login button
    And I enters valid login credentials
    And I click the "Zaloguj się" button
    Then I should see an error message "Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz."

    Examples:
      | browser |
      | Chrome  |
      | Edge |