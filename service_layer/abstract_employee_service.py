from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    # Be able to use a username and password to log in.
    @abstractmethod
    def service_employee_login(self, emp_username: str, emp_password: str):
        pass

    # Find an employee by their id.
    @abstractmethod
    def service_find_employee_per_id(self, emp_id: int):
        pass

    # Be able to submit a new reimbursement.
    @abstractmethod
    def service_submit_new_reimbursement(self, reimbursement: Reimbursement):
        pass

    # Be able to view all pending reimbursement requests per employee.
    @abstractmethod
    def service_view_pending_emp_reimbursements(self, emp_id: int):
        pass

    # Be able to view all approved reimbursement requests per employee.
    @abstractmethod
    def service_view_approved_emp_reimbursements(self, emp_id: int):
        pass

    # Be able to view all denied reimbursement requests per employee.
    @abstractmethod
    def service_view_denied_emp_reimbursements(self, emp_id: int):
        pass
