from a_entities.employee import Employee
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService
from service_layer.custom_exceptions import *


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao

    # If the username and/or password passed in from the front end has spaces, a custom exception "SpacesException" will
    # be raised. Else, if the credentials have no spaces but are still incorrect then a custom exception called
    # CredentialsFalseException will be raised. If all credentials are correct and without spaces then the manager
    # object will be returned.
    def service_manager_login(self, manager_username: str, manager_password: str):
        if " " in manager_username or " " in manager_password:
            raise SpacesException("Spaces are not allowed in username or password.")
        else:
            login = self.manager_dao.manager_login(manager_username, manager_password)
            if not login:
                raise CredentialsFalseException("The username or password is incorrect!")
            else:
                return login




    def service_all_pending_reimbursements(self):
        return self.manager_dao.all_pending_reimbursements()



    # First, try to approve the reimbursement through the dao method. If the return value is None then raise the
    # custom exception NoLongerPendingException. If the return value from the dao method is "Approved" then the approval
    # works.
    def service_approve_reimbursement(self, reimburse_id: int, reason: str):
        try_to_approve = self.manager_dao.approve_reimbursement(reimburse_id, reason)
        if try_to_approve is None:
            raise NoLongerPendingException("This reimbursement was already approved or denied!")
        else:
            return try_to_approve



    # First, try to deny the reimbursement through the dao method. If the return value is None then raise the custom
    # exception NoLongerPendingException. If the return value from the dao method is "Denied" then the denial worked.
    def service_deny_reimbursement(self, reimburse_id: int, reason: str):
        try_to_deny = self.manager_dao.deny_reimbursement(reimburse_id, reason)
        if try_to_deny is None:
            raise NoLongerPendingException("This reimbursement was already approved or denied!")
        else:
            return try_to_deny




    def service_view_approved_requests(self):
        return self.manager_dao.view_approved_requests()

    def service_view_denied_requests(self):
        return self.manager_dao.view_denied_requests()

    def service_view_all_employees(self) -> list[Employee]:
        return self.manager_dao.view_all_employees()




    # Create the list of employees and iterate through them. If one of the employee ids in the list matches the id that
    # was passed into the method then return all the reimbursements for that employee. Otherwise, raise a custom
    # exception NonExistentEmployeeException.
    def service_all_reimbursements_per_employee(self, emp_id: int):
        employee_list = self.manager_dao.all_reimbursements_per_employee(emp_id)
        if not employee_list:
            raise NonExistentEmployeeException("This employee does not exist!")
        else:
            return self.manager_dao.all_reimbursements_per_employee(emp_id)




    def service_highest_reimbursement_total(self):
        return self.manager_dao.highest_reimbursement_total()

    def service_all_requests_per_employee(self):
        return self.manager_dao.all_requests_per_employee()

    def service_dollar_total_of_approved_reimbursements(self):
        return self.manager_dao.dollar_total_of_approved_reimbursements()

    def service_employee_with_most_denials(self):
        return self.manager_dao.employee_with_most_denials()

    def service_employee_with_most_approvals(self):
        return self.manager_dao.employee_with_most_approvals()