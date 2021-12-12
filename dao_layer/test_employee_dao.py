from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

employee_dao = PostgresEmployeeDAO()


# Created reimbursement objects for testing.
create_reimbursement = Reimbursement(0, 0, "Pencils", 205.13, False)


# Test for these stories.

# as an employee, I should be able to login so I can manage my reimbursements
def test_login_happy():
    pass


# as an employee, I should be able to submit new reimbursement requests so I can get money back from the company
def test_submit_reimbursement_happy():
    new_reimbursement = employee_dao.submit_reimbursement(1, create_reimbursement)
    assert new_reimbursement.reimburse_id != 0


# as an employee, I should be able to review my reimbursement requests so I can know if they are approved or denied
def test_view_reimbursement_per_employee_happy():
    pass


def test_view_reimbursement_status_happy():
    pass


# as an employee, I should be able to logout so my information does not remain available on my computer
def test_logout_happy():
    pass