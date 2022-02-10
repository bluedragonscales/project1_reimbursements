from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO


employee_dao = PostgresEmployeeDAO()


# EMPLOYEE LOGIN TESTS
def test_employee_login_happy():
    # Pass if all credentials are correct.
    employee = employee_dao.employee_login('BeetFarmer', 'IambetterthanJim')
    assert employee

def test_employee_login_wrong_password_sad():
    # Pass if password is incorrect.
    employee = employee_dao.employee_login('BeetFarmer', 'IambetttthanJim')
    assert employee == False

def test_employee_login_wrong_username_sad():
    # Pass if username is incorrect.
    employee = employee_dao.employee_login('BetFrmer', 'IambetterthanJim')
    assert employee == False

def test_employee_login_mismatched_credentials_sad():
    # Pass if username and password are correct, but mismatched with the wrong people.
    employee = employee_dao.employee_login('BeetFarmer', 'ilovecookies<3')
    assert employee == False



# FIND EMPLOYEE TESTS
def test_find_employee_by_id_happy():
    # Pass if employee exists.
    found_employee = employee_dao.find_employee_per_id(2)
    assert found_employee.full_name == 'Jim Halpert'

def test_find_employee_by_id_sad():
    # Pass if employee does not exist.
    employee = employee_dao.find_employee_per_id(100)
    assert employee == False




# NEW REIMBURSEMENT TESTS
def test_new_reimbursement_happy():
    # Pass if information for the new reimbursement is filled out correctly.
    create_reimbursement = Reimbursement(0, 4, 9.98, '', 'girl scout cookies', '')
    new_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert new_reimbursement.amount == 9.98

def test_new_reimbursement_with_wrong_amount_sad():
    # Pass if a negative number is requested.
    create_reimbursement = Reimbursement(0, 1, -3.19, '', 'Some staples and paper reams.', '')
    another_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert another_reimbursement == False


def test_new_reimbursement_with_zero_amount_sad():
    # Pass if a zero amount is requested.
    create_reimbursement = Reimbursement(0, 100, 0, '', 'Some staples and paper reams.', '')
    another_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert another_reimbursement == False


def test_new_reimbursement_with_wrong_id_sad():
    # Pass if the employee id does not exist.
    create_reimbursement = Reimbursement(0, 200, 103.89, '', 'Some staples and paper reams.', '')
    another_reimbursement = employee_dao.submit_new_reimbursement(create_reimbursement)
    assert another_reimbursement == False




# PENDING REIMBURSEMENTS TEST
def test_view_pending_reimbursements_happy():
    pending_list = employee_dao.view_pending_emp_reimbursements(2)
    assert len(pending_list) >= 0


# APPROVED REIMBURSEMENTS TEST
def test_view_approved_reimbursements_happy():
    approved_list = employee_dao.view_approved_emp_reimbursements(3)
    assert len(approved_list) >= 0


# DENIED REIMBURSEMENTS TEST
def test_view_denied_reimbursements_happy():
    denied_list = employee_dao.view_denied_emp_reimbursements(4)
    assert len(denied_list) >= 0