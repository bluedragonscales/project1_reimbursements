# This is the framework for the actions an employee can take with the reimbursement entity plus more. They can log in to
# the reimbursement system of their company. A new reimbursement request can be submitted. They can view all of their
# reimbursement requests, and they can view their reimbursements filtered by its status.

from abc import ABC, abstractmethod
from a_entities.employee import Employee
from a_entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):

    # Be able to use a username and password to log in.
    @abstractmethod
    def employee_login(self, emp_username: str, emp_password: str):
        pass

    # Find an employee by their id.
    @abstractmethod
    def find_employee_per_id(self, emp_id: int):
        pass

    # Be able to submit a new reimbursement.
    @abstractmethod
    def submit_new_reimbursement(self, reimbursement: Reimbursement):
        pass

    # Be able to view all pending reimbursement requests.
    @abstractmethod
    def view_pending_emp_reimbursements(self, employee_id: int, pending: str) -> list[Reimbursement]:
        pass

    # Be able to view all approved reimbursement requests.
    @abstractmethod
    def view_approved_emp_reimbursements(self, employee_id: int, approved: str) -> list[Reimbursement]:
        pass

    # Be able to view all denied reimbursement requests.
    @abstractmethod
    def view_denied_emp_reimbursements(self, employee_id: int, denied: str) -> list[Reimbursement]:
        pass
