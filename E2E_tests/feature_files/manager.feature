Feature: using the manager home page in the reimbursement system.

  Scenario: As a manager I want to login so that I can access the reimbursement system.
    Given the manager is on the login page.
    When the manager inputs 2 into the manager id input box.
    When the manager inputs acapella into the password box.
    When the manager clicks the login button.
    Then the manager is redirected to the Manager Home page.

  Scenario: As a manager I want to view all reimbursement requests so that I can see all employee requests.
    Given the manager is on the Manager Home page.
    When the manager clicks on the view all reimbursements tab.
    Then the reimbursements will show and the manager will be on the Manager Home page.


  Scenario: As a manager I want to approve or deny reimbursement requests if they are legitimate or not.
    Given the manager is on the manager home page.
    When the manager clicks on the submit reimbursement status tab.
    When the manager inputs 3 in the reimbursement id input.
    When the manager selects Denied from the drop down options.
    When the manager inputs good office supplies into the reason input.
    When the manager clicks the submit status button.
    Then the status will be submitted and the manager will be on the Manager Home page.

  Scenario: As a manager I want to view reimbursement statistics so that I can keep track of employee activities.
    Given the manager is on the manager home page.
    When the manager clicks the view reimbursement statistics tab.
    When the manager selects the statistics option from the dropdown.
    When the manager clicks the statistics submit button.
    Then the statistics are shown and the manager is on the Manager Home page.

  Scenario: As a manager I want to log out so that my information will not remain on the computer.
    Given the manager is on the manager home page.
    When the manager clicks on the logout button.
    Then the manager is redirected to the Home page.