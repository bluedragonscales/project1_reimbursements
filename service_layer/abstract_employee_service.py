from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    @abstractmethod
    def service_employee_login(self, employee_id: int, password: str):
        pass

    @abstractmethod
    def service_submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass