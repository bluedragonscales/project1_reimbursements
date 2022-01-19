from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.abstract_employee_service import EmployeeService
from service_layer.custom_exceptions import *


class PostgresEmployeeService(EmployeeService):

    def __init__(self, employee_dao: PostgresEmployeeDAO):
        self.employee_dao = employee_dao



    # If the username and/or password passed in from the front end has spaces, a custom exception "SpacesException" will
    # be raised. Else, if the credentials have no spaces but are still incorrect then a custom exception called
    # CredentialsFalseException will be raised. If all credentials are correct and without spaces then the employee
    # object will be returned.
    def service_employee_login(self, emp_username: str, emp_password: str):
        if " " in emp_username or " " in emp_password:
            raise SpacesException("Spaces are not allowed in username or password.")
        else:
            login = self.employee_dao.employee_login(emp_username, emp_password)
            if not login:
                raise CredentialsFalseException("The username or password is incorrect!")
            else:
                return login



    # If no employee is found after going through the list of employees then a custom exception will be raised called
    # NonExistentEmployeeException. Else, if the employee is found then the employee object will be returned.
    def service_find_employee_per_id(self, emp_id: int):
        employee = self.employee_dao.find_employee_per_id(emp_id)
        if not employee:
            raise NonExistentEmployeeException("This employee does not exist!")
        else:
            return employee



    # If the amount of the submitted reimbursement is less than 1 a custom exception will be raised called
    # InvalidAmountException. Else if, the employee is not found in the employee list, then the
    # NonExistentEmployeeException will be raised. Otherwise, if those problems are not run into then the new
    # reimbursement object will be sent on to the dao layer and database.
    def service_submit_new_reimbursement(self, reimbursement: Reimbursement):
        if reimbursement.amount < 1:
            raise InvalidAmountException("Your reimbursement request must be greater than zero dollars!")
        elif not self.service_find_employee_per_id(reimbursement.employee_id):
            raise NonExistentEmployeeException("This employee does not exist!")
        else:
            return self.employee_dao.submit_new_reimbursement(reimbursement)



    def service_view_pending_emp_reimbursements(self, emp_id: int):
        return self.employee_dao.view_pending_emp_reimbursements(emp_id)


    def service_view_approved_emp_reimbursements(self, emp_id: int):
        return self.employee_dao.view_approved_emp_reimbursements(emp_id)


    def service_view_denied_emp_reimbursements(self, emp_id: int):
        return self.employee_dao.view_denied_emp_reimbursements(emp_id)