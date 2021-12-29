# This service layer module is the main filter through which all of the API actions get tested before working correctly.
# When a user of the front-end wants to do one of these specific features the route will send the information to this
# service layer. Exceptions will be raised if there is an error, or it will move on through to the DAO layer if there
# are no errors.

# IMPORTS
from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from service_layer.abstract_employee_service import EmployeeService
from service_layer.custom_exceptions import *


# SERVICE LAYER CLASS
class PostgresEmployeeService(EmployeeService):

    # This constructor initiates dependency injection. We're injecting the DAO class into this service class so the
    # methods in this class will work in tandem with the methods inside the DAO class.
    def __init__(self, employee_dao: PostgresEmployeeDAO):
        self.employee_dao = employee_dao


    # This service method will verify again that the password provided is correct for the employee id given. If the
    # variable "validation" comes out True after storing the results of the DAO method then we will get a return of True
    # that will be sent up to the front end. If "validation" is false then we will get a return value of False that will
    # be sent up to the front end.
    def service_employee_login(self, employee_id: int, password: str):
        validation = self.employee_dao.employee_login(employee_id, password)
        if validation:
            return True
        else:
            return False


    # This method checks to make sure that the reimbursement amount requested is greater than 0 dollars because we can't
    # have a reimbursement that is 0 or less money. Unless the employee wants to give the company money instead of the
    # other way around!
    def service_submit_new_reimbursement(self, reimburse: Reimbursement) -> Reimbursement:
        if reimburse.amount > 0:
            return self.employee_dao.submit_new_reimbursement(reimburse)
        else:
            # If 0 or less is requested as the amount, this custom exception is raised and the action of adding a new
            # reimbursement request is stopped.
            raise InvalidAmountException("Reimbursement amounts must be greater than 0.")



    # For this simple application, this method has no need for testing beyond the dao layer happy path test that has
    # already been done, so we just slide it through the service layer to the dao layer.
    def service_view_pending_emp_reimbursements(self, employee_id: int, pending: str) -> list[Reimbursement]:
        return self.employee_dao.view_pending_emp_reimbursements(employee_id, pending)

    # For this simple application, this method has no need for testing beyond the dao layer happy path test that has
    # already been done, so we just slide it through the service layer to the dao layer.
    def service_view_approved_emp_reimbursements(self, employee_id: int, approved: str) -> list[Reimbursement]:
        return self.employee_dao.view_approved_emp_reimbursements(employee_id, approved)

    # For this simple application, this method has no need for testing beyond the dao layer happy path test that has
    # already been done, so we just slide it through the service layer to the dao layer.
    def service_view_denied_emp_reimbursements(self, employee_id: int, denied: str) -> list[Reimbursement]:
        return self.employee_dao.view_denied_emp_reimbursements(employee_id, denied)