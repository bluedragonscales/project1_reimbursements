from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    @abstractmethod
    def service_login(self, employee_id: int):
        pass

    @abstractmethod
    def service_submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_reimbursement_status(self, reimburse_id: int):
        pass

    @abstractmethod
    def service_logout(self, employee_id):
        pass