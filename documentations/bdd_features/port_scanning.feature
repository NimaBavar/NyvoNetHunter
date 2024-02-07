# language: en


Feature: The open_port scanning feature.


Rule: The user cannot start a new searching session while a port_scanning operatin is running.
    
  Example:
    Given a searching session have finished
    When Ali clicks the scan ports button
    Then the search button will be disabled and unclickable.


Rule: The user is only able to scan for open ports after a searching operation.
  
  Example:
    When Ali clicks the search operation
    And a valid response is received

    Then the scan ports button will be enabled.


Scenario: The user is able to cancel the port scanning operation.
    
  Given a port_scanning operation is running
  When Ali clicks the cancel scanning button
  Then the port scanning operation will be cancelled.


Scenario The user can scan for open ports.

  When Ali clicks the scan ports button
  Then all of the breachable open ports related to the searched element will be visualized.
