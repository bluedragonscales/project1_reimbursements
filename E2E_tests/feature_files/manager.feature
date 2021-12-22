Feature: using the manager home page in the reimbursement system.

  Scenario: As a manager I want to login so that I can view all the reimbursements requested.
    Given the manager is on the login page.
    When the manager fills in id in the input space.
    When the manager fills in password in the input space.
    When the manager clicks the login button.
    Then the manager will be redirected to the manager home page.

  Scenario: As a manager I want to approve or deny reimbursement requests if they are legitimate or not.
    Given the manager is on the manager home page.
    When the manager clicks on the submit reimbursement status tab.
    When the manager fills out the reimbursement id.
    When the manager selects approved or denied from the drop down options.
    When the manager fills out the reason input.
    When the manager clicks the submit status button.
    Then the status will be submitted.

  Scenario: As a manager I want to view reimbursement statistics so that I can keep track of employee activities.
    Given the manager is on the manager home page.
    When the manager clicks the view reimbursement statistics tab.
    When the manager selects the statistics option from the dropdown.
    When the manager clicks the statistics submit button.
    Then the statistics are shown.

  Scenario: As a manager I want to log out so that my information will not remain on the computer.
    Given the manager is on the manager home page.
    When the manager clicks on the logout button.
    Then the manager is redirected to the login page.