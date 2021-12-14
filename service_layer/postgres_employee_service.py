from a_entities.reimbursement import Reimbursement
from service_layer.abstract_employee_service import EmployeeService


class PostgresEmployeeService(EmployeeService):
    
    def service_login(self, employee_id: int):
        pass

    def service_submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass

    def service_view_reimbursement_status(self, reimburse_id: int):
        pass

    def service_logout(self, employee_id):
        pass