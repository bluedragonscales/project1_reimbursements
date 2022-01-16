from a_entities.employee import Employee
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService
from service_layer.custom_exceptions import *


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao


    def service_manager_login(self, manager_username: str, manager_password: str):
        pass

    # Be able to view all reimbursements that are pending.
    def service_all_pending_reimbursements(self):
        pass

    # Be able to approve a reimbursement request made by an employee and give a reason.
    def service_approve_reimbursement(self, reimburse_id: int, reason: str):
        pass

    # Be able to deny a reimbursement request made by an employee and give a reason.
    def service_deny_reimbursement(self, reimburse_id: int, reason: str):
        pass

    # Be able to view all past approved reimbursement requests.
    def service_view_approved_requests(self):
        pass

    # Be able to view all past denied reimbursement requests.
    def service_view_denied_requests(self):
        pass

    # To see all reimbursements for each employee individually.
    def service_all_reimbursements_per_employee(self, emp_id: int):
        pass

    # To get an employee list for functionality.
    def service_view_all_employees(self) -> list[Employee]:
        pass

    # To show which employee has requested the highest dollar total in reimbursements.
    def service_highest_reimbursement_total(self):
        pass

    # To show which employee has made the most reimbursement requests.
    def service_all_requests_per_employee(self):
        pass

    # To show the total dollar amount of all reimbursements approved.
    def service_dollar_total_of_approved_reimbursements(self):
        pass

    # To show which employee has the most denials.
    def service_employee_with_most_denials(self):
        pass

    # To show which employee has the most approvals.
    def service_employee_with_most_approvals(self):
        pass