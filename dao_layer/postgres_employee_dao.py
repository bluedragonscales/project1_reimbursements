from a_entities.employee import Employee
from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO
from database_connection import connection


# DAO LAYER CLASS
class PostgresEmployeeDAO(EmployeeDAO):

    # If the username entered does not exist in the database the method will return false. If the username exists it
    # will pull up the credentials for that employee. If the password entered does not match the password for that
    # employee the method will return false. If the username and password are correct and correlated to the same
    # employee then the employee object will be returned.
    def employee_login(self, emp_username: str, emp_password: str):
        sql = 'select * from employee where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [emp_username])
        employee_record = cursor.fetchone()
        if employee_record:
            employee = Employee(*employee_record)
            if employee.password == emp_password:
                return employee
            else:
                return False
        else:
            return False



    # This method will be used with other methods to verify the employee exists. If the employee id pulls up an employee
    # in the database it will return that employee object. If the id does not exist then the method will return false.
    def find_employee_per_id(self, emp_id: int):
        sql = 'select * from employee where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        emp_record = cursor.fetchone()
        if emp_record:
            employee = Employee(*emp_record)
            return employee
        else:
            return False




    # If the reimbursement amount is 0 or less then the method will return false. If the amount entered is greater
    # than 0 then we search for the employee that is requesting the reimbursement. If they exist in the database then
    # the values for the reimbursement will be entered and a new reimbursement request will be created. If the employee
    # doesn't exist in the database then the method will return false.
    def submit_new_reimbursement(self, reimbursement: Reimbursement):
        if reimbursement.amount > 0:
            real_employee = self.find_employee_per_id(reimbursement.employee_id)
            if real_employee:
                sql = 'insert into reimbursement values(default, %s, %s, default, %s, default) returning reimburse_id'
                cursor = connection.cursor()
                cursor.execute(sql, (reimbursement.employee_id, reimbursement.amount, reimbursement.emp_reason))
                reimburse_id = cursor.fetchone()[0]
                reimbursement.reimburse_id = reimburse_id
                connection.commit()
                return reimbursement
            else:
                return False
        else:
            return False




    def view_pending_emp_reimbursements(self, emp_id: int):
        sql = "select * from reimbursement where employee_id = %s and status = 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        reimburse_records = cursor.fetchall()
        pending_reimbursements_list = []
        for pending in reimburse_records:
            pending_reimbursements_list.append(Reimbursement(*pending))
        return pending_reimbursements_list




    def view_approved_emp_reimbursements(self, emp_id: int):
        sql = "select * from reimbursement where employee_id = %s and status = 'Approved'"
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        reimburse_records = cursor.fetchall()
        approved_reimbursements_list = []
        for approved in reimburse_records:
            approved_reimbursements_list.append(Reimbursement(*approved))
        return approved_reimbursements_list





    def view_denied_emp_reimbursements(self, emp_id: int):
        sql = "select * from reimbursement where employee_id = %s and status = 'Denied'"
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        reimburse_records = cursor.fetchall()
        denied_reimbursements_list = []
        for denied in reimburse_records:
            denied_reimbursements_list.append(Reimbursement(*denied))
        return denied_reimbursements_list