from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_employee_service import PostgresEmployeeService

employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)



def test_service_login():
    pass


def test_validate_submit_reimbursement():
    try:
        wrong_reimburse_info = Reimbursement(0, 1, "More pencils", -20.10, "Pending")
        employee_service.service_submit_reimbursement(wrong_reimburse_info)
    except InvalidAmountException as a:
        assert str(a) == "Reimbursement requests must be greater than 0."
    # Test to make sure a negative amount is not being requested.
    # If there is time at the end, change it so that Pending is added to the status automatically.


def test_validate_view_reimbursement_per_employee():
    try:
        employee_service.service_view_reimbursement_per_employee(1)
    except ListUnavailableException as u:
        assert str(u) == "You have not made any reimbursement requests."
    # Test to make sure the employee has actually made requests.



def test_service_logout():
    pass