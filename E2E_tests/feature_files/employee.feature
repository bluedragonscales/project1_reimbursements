Feature: Using the employee home page in the reimbursement system.

  Scenario: As an employee I want to login so that I can access the reimbursement system.
    Given the employee is on the login page
    When the employee inputs 7 into the employee id input box
    When the employee inputs whatever into the password input box
    When the employee clicks the login button
    Then the employee is redirected to the Employee Home page

  Scenario: As an employee I want to submit a new reimbursement request to get money back from the company.
    Given the employee is on the employee home page
    When the employee clicks the request reimbursement tab
    When the employee inputs office supplies in the request purpose input
    When the employee inputs 46.89 in the amount input
    When the employee clicks the submit reimbursement button
    Then a new reimbursement request has been submitted and the employee is on the Employee Home page

  Scenario: As an employee I want to view my submitted reimbursement requests so that I know if they were approved or denied.
    Given the employee is on the employee home page
    When the employee clicks the view reimbursements tab
    Then the reimbursements are shown and the employee is on the Employee Home page

  Scenario: As an employee I want to logout so that my information will not remain on the computer.
    Given the employee is on the employee home page
    When the employee clicks on the logout button
    Then the employee will be redirected to the index Home page