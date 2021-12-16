from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

employee_dao = PostgresEmployeeDAO()


# Created reimbursement objects for testing.
create_reimbursement = Reimbursement(0, 9, "test this request deletion", 110.13, "")



def test_employee_login_happy():
    credentials = employee_dao.employee_login(7)
    assert credentials[1] == "whatever"



def test_submit_reimbursement_happy():
    new_reimbursement = employee_dao.submit_reimbursement(create_reimbursement)
    assert new_reimbursement.reimburse_id != 0



def test_view_reimbursement_per_employee_happy():
    reimburse_list_for_employee = employee_dao.view_reimbursement_per_employee(4)
    assert len(reimburse_list_for_employee) > 0