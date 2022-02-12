import pytest

from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_employee_service import PostgresEmployeeService

employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)



# SERVICE TESTS FOR LOGGING IN
def test_validate_employee_cant_login_with_incorrect_credentials():
    try:
        employee_service.service_employee_login('BeetFarmer', 'ILoveJim<3')
        assert False
    except CredentialsFalseException as c:
        assert str(c) == "The username or password is incorrect!"


def test_validate_employee_cant_login_with_spaces():
    with pytest.raises(SpacesException):
        employee_service.service_employee_login('Angela Cat', 'ilovecats<3')




# SERVICE TESTS FOR EMPLOYEE EXISTENCE
def test_validate_employee_id_doesnt_exist():
    try:
        employee_service.service_find_employee_per_id(200)
        assert False
    except NonExistentEmployeeException as n:
        assert str(n) == "This employee does not exist!"




# SERVICE TESTS FOR CREATING NEW REIMBURSEMENT
def test_amount_requested_wrong_amount():
    try:
        wrong_amount = Reimbursement(0, 1, -32.19, '', 'Some staples and paper reams.', '')
        employee_service.service_submit_new_reimbursement(wrong_amount)
        assert False
    except InvalidAmountException as i:
        assert str(i) == "Your reimbursement request must be greater than zero dollars!"


def test_validate_wrong_employee_id():
    try:
        wrong_emp_request = Reimbursement(0, 200, 103.89, '', 'Some staples and paper reams.', '')
        employee_service.service_submit_new_reimbursement(wrong_emp_request)
        assert False
    except NonExistentEmployeeException as n:
        assert str(n) == "This employee does not exist!"

