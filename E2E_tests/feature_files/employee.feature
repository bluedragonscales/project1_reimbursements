Feature: Using the employee home page in the reimbursement system.

  Scenario: As an employee I want to login so that I can view my reimbursements.

    Given the employee is on the login page.
    When the employee fills in the employee id.
    When the employee fills in the password.
    When the employee clicks the log in button.
    Then the employee is redirected to the employee home page.

  Scenario: As an employee I want to submit a new reimbursement request to get money back from the company.

    Given the employee is on the submit request page.
    When the employee fills in the request purpose.
    When the employee fills in the amount.
    When the employee clicks the submit button.
    Then a new request is submitted.

  Scenario: As an employee I want to view my submitted reimbursement requests so that I know if they were approved or denied.

    Given the employee is on the employee home page.
    When the employee clicks the view reimbursements button.
    Then the reimbursements are shown.

  Scenario: As an employee I want to log out so that my information will not remain on the computer.

    Given the employee is on the employee home page.
    When the employee clicks on the log out button.
    Then they will be logged out.