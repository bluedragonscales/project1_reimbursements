from a_entities import reimbursement
from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.abstract_employee_service import EmployeeService
from service_layer.custom_exceptions import *


class PostgresEmployeeService(EmployeeService):

    def __init__(self, employee_dao):
        self.employee_dao: PostgresEmployeeDAO = employee_dao


    def service_login(self, employee_id: int):
        return self.employee_dao.login(employee_id)


    def service_submit_reimbursement(self, reimburse: Reimbursement) -> Reimbursement:
        if reimburse.amount > 0:
            return self.employee_dao.submit_reimbursement(reimburse)
        else:
            raise InvalidAmountException("Reimbursement requests must be greater than 0.")


    def service_view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        if employee_id != reimbursement.employee_id:
            raise ListUnavailableException("You have not made any reimbursement requests.")
        else:
            return self.employee_dao.view_reimbursement_per_employee(employee_id)


    def service_logout(self, employee_id):
        return self.employee_dao.logout(employee_id)