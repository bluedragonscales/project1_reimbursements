from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.abstract_employee_service import EmployeeService
from service_layer.custom_exceptions import *


class PostgresEmployeeService(EmployeeService):

    def __init__(self, employee_dao: PostgresEmployeeDAO):
        self.employee_dao = employee_dao



    def service_employee_login(self, emp_username: str, emp_password: str):
        pass



    def service_find_employee_per_id(self, emp_id: int):
        pass



    def service_submit_new_reimbursement(self, reimbursement: Reimbursement):
        pass



    def service_view_pending_emp_reimbursements(self, emp_id: int):
        pass



    def service_view_approved_emp_reimbursements(self, emp_id: int):
        pass



    def service_view_denied_emp_reimbursements(self, emp_id: int):
        pass