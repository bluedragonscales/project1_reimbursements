from abc import ABC, abstractmethod

from a_entities.employee import Employee
from a_entities.reimbursement import Reimbursement


class ManagerDAO(ABC):

    # Be able to use a username and password to log in.
    @abstractmethod
    def manager_login(self, manager_username: str, manager_password: str):
        pass

    # Be able to view all reimbursements that are pending approval.
    @abstractmethod
    def all_pending_reimbursements(self):
        pass

    # Be able to approve a reimbursement request made by an employee and give a reason.
    @abstractmethod
    def approve_reimbursement(self, reimburse_id: int, reason: str):
        pass

    # Be able to deny a reimbursement request made by an employee and give a reason.
    @abstractmethod
    def deny_reimbursement(self, reimburse_id: int, reason: str):
        pass

    # Be able to view all past approved reimbursement requests.
    @abstractmethod
    def view_approved_requests(self):
        pass

    # Be able to view all past denied reimbursement requests.
    @abstractmethod
    def view_denied_requests(self):
        pass

    # To see all reimbursements for each employee individually.
    @abstractmethod
    def all_reimbursements_per_employee(self, emp_id: int):
        pass

    # To get an employee list for functionality.
    @abstractmethod
    def view_all_employees(self) -> list[Employee]:
        pass

    # To show which employee has requested the highest dollar total in reimbursements.
    @abstractmethod
    def highest_reimbursement_total(self):
        pass

    # To show which employee has made the most reimbursement requests.
    @abstractmethod
    def all_requests_per_employee(self):
        pass

    # To show the total dollar amount of all reimbursements approved.
    @abstractmethod
    def dollar_total_of_approved_reimbursements(self):
        pass

    # To show which employee has the most denials.
    @abstractmethod
    def employee_with_most_denials(self):
        pass

    # To show which employee has the most approvals.
    @abstractmethod
    def employee_with_most_approvals(self):
        pass


