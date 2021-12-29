# This is the data access object layer test module. These happy path unit tests will make sure all of the methods
# created in the "postgres_employee_dao" module will work perfectly when correct information is passed in.

from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

# This is the object created from the "PostgresEmployeeDAO" class which is needed to use the methods in that class for
# the tests to run properly.
employee_dao = PostgresEmployeeDAO()


# This is a temporary reimbursement object created to use with the submit new reimbursement test
create_reimbursement = Reimbursement(0, 4, "cookies", 22.99, "", '')



def test_employee_login_happy():
    valid_login = employee_dao.employee_login(6, "whatever")
    assert valid_login



def test_submit_new_reimbursement_happy():
    new_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert new_reimbursement.request_label == "cookies"



def test_view_pending_emp_reimbursements_happy():
    pending_list = employee_dao.view_pending_emp_reimbursements(2, 'Pending')
    assert len(pending_list) >= 0



def test_view_approved_emp_reimbursements_happy():
    approved_list = employee_dao.view_approved_emp_reimbursements(3, 'Approved')
    assert len(approved_list) >= 0



def test_view_denied_emp_reimbursements_happy():
    denied_list = employee_dao.view_denied_emp_reimbursements(4, 'Denied')
    assert len(denied_list) >= 0