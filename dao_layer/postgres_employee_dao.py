from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO


class PostgresEmployeeDAO(EmployeeDAO):

    def login(self, employee_id: int):
        pass

    def submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass

    def view_reimbursement_status(self, reimburse_id: int):
        pass

    def logout(self, employee_id):
        pass