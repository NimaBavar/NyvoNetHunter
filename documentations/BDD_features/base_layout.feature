# language: en

Feature: The apps base layout algorithm.


Scenario: User launches the app
  Given the User launches the app
    When Python is allready installed 
      And all requirements are satisfied
        """Scenario implemented"""

    
    But if requirements are not satisfied or python is not installed
      """Scenario implemented."""


Scenario: The requirements are not satisfied Or/And Python is not installed
  Given the requirements are not satisfied or Python is not installed
    When the user accepted and gave permission to install the requirements
      Then install the requirements
        But do not launch the app.

    
    But if the user rejected and denied the permission required for installing the requirements
      Then Warn the user
        And app launcher

    
Scenario: All of the requirements are satisfied and Python is installed
  Given all of the the requirements are satisfied
    Then show the acount management panel