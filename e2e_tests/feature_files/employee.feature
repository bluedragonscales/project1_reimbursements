Feature: Employee portal for reimbursements

  Scenario: As an employee I want to log in so that I can manage my reimbursement requests
    Given the employee is on the login page
    When the employee types their username into the username input
    When the employee types their password into the password input
    When the employee clicks on the login button
    Then the employee is redirected to the employee portal home page

  Scenario: As an employee I want to submit a reimbursement request so that I can get money back from the company
    Given the employee is on the employee portal home page
    When the employee clicks the new reimbursement tab
    When the employee types the reason into the reason input
    When the employee types the amount into the amount input
    When the employee clicks the submit button
    Then a success message will populate

  Scenario Outline: As an employee I want to check my past reimbursement requests to see if they were approved or denied
    Given the employee is on the employee portal home page
    When the employee clicks the <value> reimbursements tab
    Then the <value2> reimbursements will populate

    Examples:
      | value    | value2   |
      | Pending  | Pending  |
      | Approved | Approved |
      | Denied   | Denied   |


    Scenario: As an employee I want to log out so that my information is not saved on the computer
      Given the employee is on the employee portal home page
      When the employee clicks the log out tab
      Then the employee will be redirected to the login page
