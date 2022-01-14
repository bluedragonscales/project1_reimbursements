# project1_reimbursements
Second 3 tier web app

This is a project that features the ability to create and review reimbursements. Employees of a this fictional company can request reimbursements for things they bought for the sake of work. Managers of those employees can accept or reject the reimbursement requests depending on whether or not they believe the requests are legitimate.

### User Stories
- Employees
    - as an employee, I should be able to login so I can manage my reimbursements
    - as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
    - as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
    - as an employee, I should be able to logout so my information does not remain available on my computer
- Managers
    - as a manager, I should be able to login so I can approve or deny reimbursements
    - as a manager, I should be able to approve reimbursement requests because they are legitamate
    - as a manager, I should be able to deny reimbursement requests because they are illegitamate
    - as a manager, I should be able to leave a comment about my decisions regarding reimbursement requests so employees better understand my decisions
    - as a manager, I should be able to view pending reimbursement requests so I can make decisions about them
    - as a manager, I should be able to view past reimbursement requests so I can check previous decisions
    - as a manager, I should be able to view reimbursement statistics so I can keep track of employee acitvities
    - as a manager, I should be able to log out so my information does not remain available on my computer
- System
    - as the system, I should reject failed login attempts
    - as the system, I should reject negative values for reimbursement requests
    - as the system, I should reject non-numeric values for reimbursement requests


These are the tables I created in the database for this project.

![PostgreSQL tables](/front-end/images/db-tables.jpg)
