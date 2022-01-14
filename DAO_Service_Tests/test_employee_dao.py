# This is the data access object layer test module. These happy path unit tests will make sure all of the methods
# created in the "postgres_employee_dao" module will work perfectly when correct information is passed in.

from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO

# This is the object created from the "PostgresEmployeeDAO" class which is needed to use the methods in that class for
# the tests to run properly.
employee_dao = PostgresEmployeeDAO()

# LOGIN TESTS
def test_employee_login_happy():
    employee = employee_dao.employee_login('BeetFarmer', 'IambetterthanJim')
    assert employee

def test_employee_login_wrong_password_sad():
    employee = employee_dao.employee_login('BeetFarmer', 'IambetttthanJim')
    assert employee == False

def test_employee_login_wrong_username_sad():
    employee = employee_dao.employee_login('BetFrmer', 'IambetterthanJim')
    assert employee == False


# FIND EMPLOYEE TESTS
def test_find_employee_by_id_happy():
    assert employee_dao.find_employee_per_id(2)

def test_find_employee_by_id_sad():
    employee = employee_dao.find_employee_per_id(100)
    assert employee == False


# NEW REIMBURSEMENT TESTS
def test_submit_new_reimbursement_happy():
    create_reimbursement = Reimbursement(0, 4, 22.99, '', 'i want mor cookies for the ofice', '')
    new_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert new_reimbursement.amount == 22.99

def test_submit_new_reimbursement_sad():
    create_reimbursement = Reimbursement(0, 1, -3.19, '', 'Some staples and paper reams.', '')
    another_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert another_reimbursement == False




# def test_view_pending_emp_reimbursements_happy():
#     pending_list = employee_dao.view_pending_emp_reimbursements(2, 'Pending')
#     assert len(pending_list) >= 0
#
#
# def test_view_approved_emp_reimbursements_happy():
#     approved_list = employee_dao.view_approved_emp_reimbursements(3, 'Approved')
#     assert len(approved_list) >= 0
#
#
# def test_view_denied_emp_reimbursements_happy():
#     denied_list = employee_dao.view_denied_emp_reimbursements(4, 'Denied')
#     assert len(denied_list) >= 0
