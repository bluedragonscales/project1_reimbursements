Feature: Manager portal for approving and disapproving reimbursements

  Scenario: As a manager I want to log in so that I can check reimbursement requests from employees
    Given the manager is on the login page
    When the manager types their username into the username input
    When the manager types their password into the password input
    When the manager clicks the login button
    Then the manager will be redirected to the manager portal home page

  Scenario: As a manager I want to approve reimbursement requests so that I can acknowledge them as legitimate
    Given the manager is on the manager portal home page
    When the manager clicks on the pending reimbursements tab
    When the manager types the reimbursement id into the id input
    When the manager types their reasoning into the reason input
    When the manager clicks the approve button
    Then an approved message appears

  Scenario: As a manager I want to deny reimbursement requests so that I can acknowledge them as illegitimate
    Given the manager is on the manager portal home page
    When the manager clicks on the pending reimbursements tab
    When the manager types the bad reimburse id into the id input
    When the manager types a reason for denial into the reason input
    When the manager clicks the deny button
    Then a denied message appears

  Scenario: As a manager I want to view past reimbursement requests so that I can view past decisions
    Given the manager is on the manager portal home page
    When the manager clicks on the past reimbursements tab
    Then the past approved reimbursements populate
    Then the past denied reimbursements populate

  Scenario: As a manager I want to log out so that my information does not remain on my computer
    Given the manager is on the manager portal home page
    When the manager clicks on the log out tab
    Then the manager is redirected to the login page