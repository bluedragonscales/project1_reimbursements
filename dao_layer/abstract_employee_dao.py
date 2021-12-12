from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):

    @abstractmethod
    def login(self, employee_id: int):
        pass

    @abstractmethod
    def submit_reimbursement(self, employee_id: int, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_reimbursement_status(self, reimburse_id: int):
        pass

    @abstractmethod
    def logout(self, employee_id):
        pass