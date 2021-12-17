from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_employee_service import EmployeeService
from service_layer.custom_exceptions import *


class PostgresEmployeeService(EmployeeService):

    def __init__(self, employee_dao):
        self.employee_dao: PostgresEmployeeDAO = employee_dao


    def service_employee_login(self, employee_id: int, password: str):
        validation = self.employee_dao.employee_login(employee_id, password)
        if validation:
            return True
        else:
            return False


    def service_submit_reimbursement(self, reimburse: Reimbursement) -> Reimbursement:
        if reimburse.amount > 0:
            return self.employee_dao.submit_reimbursement(reimburse)
        else:
            raise InvalidAmountException("Reimbursement requests must be greater than 0.")



    def service_view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        return self.employee_dao.view_reimbursement_per_employee(employee_id)