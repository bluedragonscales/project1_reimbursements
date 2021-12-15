from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

employee_dao = PostgresEmployeeDAO()


# Created reimbursement objects for testing.
create_reimbursement = Reimbursement(0, 9, "test this request deletion", 110.13, "")


# as an employee, I should be able to login so I can manage my reimbursements
def test_login_happy():
    pass



def test_submit_reimbursement_happy():
    new_reimbursement = employee_dao.submit_reimbursement(create_reimbursement)
    assert new_reimbursement.reimburse_id != 0



def test_view_reimbursement_per_employee_happy():
    reimburse_list_for_employee = employee_dao.view_reimbursement_per_employee(4)
    assert len(reimburse_list_for_employee) > 0



# as an employee, I should be able to logout so my information does not remain available on my computer
def test_logout_happy():
    pass