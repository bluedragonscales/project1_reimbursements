# from a_entities.reimbursement.py import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

employee_dao = PostgresEmployeeDAO()



# Test for these stories.

# as an employee, I should be able to login so I can manage my reimbursements
def test_login():
    pass


# as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
def test_submit_reimbursement():
    pass

# as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
def test_view_reimbursement_per_employee():
    pass


def test_view_reimbursement_status():
    pass


# as an employee, I should be able to logout so my information does not remain available on my computer
def test_logout():
    pass