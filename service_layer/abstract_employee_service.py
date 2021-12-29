# This is the service framework for the actions an employee will be taking with the reimbursement entity and whether
# they will work correctly. These abstract methods for the service layer only provides the function of better
# organization for this program.

from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    @abstractmethod
    def service_employee_login(self, employee_id: int, password: str):
        pass

    @abstractmethod
    def service_submit_new_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def service_view_pending_emp_reimbursements(self, employee_id: int, pending: str) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_approved_emp_reimbursements(self, employee_id: int, approved: str) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_denied_emp_reimbursements(self, employee_id: int, denied: str) -> list[Reimbursement]:
        pass