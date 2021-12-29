from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_employee_service import PostgresEmployeeService

employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)



def test_validate_employee_login():
    not_validated = employee_service.service_employee_login(6, "watevr")
    assert not_validated == False



def test_validate_submit_new_reimbursement():
    try:
        wrong_reimburse_info = Reimbursement(0, 3, "More pencils", -20.10, "", '')
        employee_service.service_submit_new_reimbursement(wrong_reimburse_info)
    except InvalidAmountException as a:
        assert str(a) == "Reimbursement amounts must be greater than 0."

