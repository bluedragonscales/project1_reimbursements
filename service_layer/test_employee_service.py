from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_employee_service import PostgresEmployeeService

employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)



def test_validate_employee_login():
    pass
# Test if the employee uses the right credentials.


def test_validate_submit_reimbursement():
    try:
        wrong_reimburse_info = Reimbursement(0, 1, "More pencils", -20.10, "")
        employee_service.service_submit_reimbursement(wrong_reimburse_info)
    except InvalidAmountException as a:
        assert str(a) == "Reimbursement requests must be greater than 0."

