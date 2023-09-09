Feature: Testing Movie API

  Scenario: Access the '/movies/best/<n>' endpoint
    Given I am using the movie API
    When I access the '/movies/best/<n>' endpoint
    Then the API only shows me the movies <movielist> sorted by rating and then by metascore

  Scenario: Access the '/movies/best/' endpoint
    Given I am using the movie API
    When I access the '/movies/best/' endpoint
    Then the API shows me the top 10 movies sorted by rating and then by metascore
