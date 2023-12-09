# language: en

Feature: The apps base layout algorithm.


Background:


  Scenario: User launches the app
    When the User launches the app
      Then launch the app.


  Scenario: The requirements are not satisfied Or/And Python is not installed
    When the requirements are not satisfied or Python is not installed
      When the user accepted and gave permission to install the requirements
        Then install the requirements
          But do not launch the app.

    
      But if the user rejected and denied the permission required for installing the requirements
        Then Warn the user
          And close the app launcher.

    
  Scenario: All of the requirements are satisfied and Python is installed
    When all of the the requirements are satisfied
      Then show the acount management panel.

    
  Scenario: The User decides to quit
    When the User clicks the close button
      When all safety checking operations succeded
        Then close the application.
  

  Scenario: Not internet connection is found
    When the user does not have any internet connection
      Then suspend the app until the internet connection becomes accessible.


Scenario: The User chose the login option
  Given the account management panel is launched
    When the User chose the login option
      Then verify the User information
        When the Information is valid
          Then log the user into the application

        But if the information is not valid
          Then warn the user to try again.


Scenario: The User chose the sign-up option
  When the account management panel is launched
    When the User chose the sign-up option
      Then Verify the user sign-up inputs
        When the sign-ip inputs are valid
          Then create the User account
            And log the user in.

        But if the inputs are invalid
          Then warn the User to try again.


Scenario: The user is logged in
  Given the user is logged in
    And internet connection is available
      Then show the apps main panle


Scenario: The main panel is launched
  When the main panel is launched
    Then show the input form
      And show the 'Generate' button.


Scenario: The user input is valid
  When the user input is valid
    Then warn the user that their input is valid
      And unlock the 'Generate' button.


Scenario: The user input is invalid or contains sensitive content
  When the user input is invalid or contains sensitive content
    Then warn the user that their input is invalid
      And lock 'Generate' button.
  

Scenario: The user clicks the generate buttion
  When the user clicks the generate button
    Then produce a AI generated image
      And display the image on the screen.



"""ALGORITHM BY: KHODENIMA ( NIMA BAVAR )"""
