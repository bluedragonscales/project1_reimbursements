from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):

    @abstractmethod
    def employee_login(self, employee_id: int):
        pass

    @abstractmethod
    def submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass