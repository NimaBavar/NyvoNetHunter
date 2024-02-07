# language: en

Feature: The apps fundamental features.


Background: The app must be launched at first.


Rule: The user is unable to use the app features without a valid internet connection.

  Example: Ali cannot dig an URL address without internet connection.
    When Ali does not have a valid internet connection
    Then all the app features will be locked.
    

Rule: The user cannot examine a network endpoint without choosing at least one examine option.

  Example: Ali cannot examine an URL address without chosing at least one examine option
    When all examine options are unchecked
    When Ali tries to examine the information of: "https://google.com"
    Then he will be informed with an error message on the response screen.
    

Rule: The user cannot examine the informations of an invalid IP or URL address

  Example: Ali cannot examine an invalid URL address
    When Ali tries to examine the information of: "I'm an invalid IP address!"
    Then he will be informed with an error message on the response screen.
    

Rule: The user cannot see the in-map location of an endpoint if the required informations couldn't be found.
  
  Example: Ali cannot see the in-map location of an URL address if the lattitude and the longitude are not found
    Given the "Show map location" option is checked
    When Ali tries to examine the information of: "https://github.com/KhodeNima"
    But the lattitude and longitude couldn't be found
    
    Then Ali will be informed with an error message on the map screen.
    

Rule: The user cannot rapidly examine an endpoint

  Example: Ali cannot examine the URL "https://github.com/KhodeNima" three times in less than 10 second
    When Ali examines the URL "https://github.com/KhodeNima"
    And he perform the exmination option again "https://github.com/KhodeNima"
    And he perform it again
    
    Then Ali will be informed with an error message on the response screen.
      

Scenario: the user can see his/her internet connection status on the main window.

  When the user does not have an internet connection
  Then the no connection movie will start.
    
  But if the user have a strong enough internet connection
  Then the connection movie will start.
    
    
Scenario: The user can examine the informations of an IP address.

  When Ali inputs the IP address: 144.145.146.147
  And clicks the examine button
    
  Then the IP information will be visible on the response screen.
  
  
Scenario: The user can examine the informations of an URL address.

  When Ali inputs the URL address: "https://github.com/KhodeNima"
  And clicks the examine button
    
  Then the URL information will be visible on the response screen.
    

Scenario: The user can see the in-map location of the examined endpoint.
  
  When Ali input the URL address: "https://google.com"
  And he chekcs the examine option: "Show map location"
  And lattitude of the URL is found
  And the longitude of the URL is found
  
  Then show the exact in-map location of the URL on the map screen.


"""ALGORITHM EXPLANATION BY: KHODENIMA ( NIMA BAVAR )"""
