# This is the framework for the actions an employee can take with the reimbursement entity plus more. They can log in to
# the reimbursement system of their company. A new reimbursement request can be submitted. They can view all of their
# reimbursement requests, and they can view their reimbursements filtered by its status.

from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):

    @abstractmethod
    def employee_login(self, employee_id: int, password: str):
        pass

    @abstractmethod
    def submit_new_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def view_pending_emp_reimbursements(self, employee_id: int, pending: str) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_approved_emp_reimbursements(self, employee_id: int, approved: str) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_denied_emp_reimbursements(self, employee_id: int, denied: str) -> list[Reimbursement]:
        pass
