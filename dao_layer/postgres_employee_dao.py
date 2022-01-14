# This is the main implementation of the employee's actions with the reimbursement entity, and this is where information
# is passed back and forth through the DBeaver database management system (hosted through AWS) using PostgreSQL.

# IMPORTS
from a_entities.employee import Employee
from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO
from database_connection import connection


# DAO LAYER CLASS
class PostgresEmployeeDAO(EmployeeDAO):

    # This method validates the login. When an employee gives their username it pulls up the employee's information. If
    # the password the employee provided matches the one in the database then the whole employee entity is returned.
    def employee_login(self, emp_username: str, emp_password: str):
        sql = 'select * from employee where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [emp_username])
        employee_record = cursor.fetchone()
        if employee_record:
            employee = Employee(*employee_record)
            if employee.username == emp_username and employee.password == emp_password:
                return employee
            else:
                return False
        else:
            return False



    # This method will be used with other methods to verify the employee exists.
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




    # This method handles the creation of a new reimbursement object and stores it in the database. It takes in only
    # three initial values because the other three are default. The first default is the reimbursement id and that is a
    # serial created in PostgreSQL. The second default is the status which is initialized to pending and will be
    # modified when the manager approves or denies the reimbursement. The third default is the reason which is first
    # initialized to pending but will be changed to a reason why the manager approved or denied the reimbursement
    # request.
    def submit_new_reimbursement(self, reimbursement: Reimbursement):
        real_employee = self.find_employee_per_id(reimbursement.employee_id)
        if real_employee and reimbursement.amount > 0:
            sql = 'insert into reimbursement values(default, %s, %s, default, %s, default) returning reimburse_id'
            cursor = connection.cursor()
            # The defaults don't need arguments to pass to them so we only send in the reimbursement's values that had
            # to be initialized through the employee's creation process.
            cursor.execute(sql, (reimbursement.employee_id, reimbursement.amount, reimbursement.emp_reason))
            # Since the reimbursement id is a serial created by the database, it has to be reassigned to the actual
            # reimbursement object here in Python. So we grab the value that was returned with the sql statement and
            # then assign it to the reimbursement object.
            reimburse_id = cursor.fetchone()[0]
            reimbursement.reimburse_id = reimburse_id
            connection.commit()
            # We send the full reimbursement object back up to the API so that it can be viewed on the website.
            return reimbursement
        else:
            return False




    # This method handles populating the reimbursement requests, per employee, that are pending. We pass in the employee
    # id to pick the employee that wants to see their reimbursements. We pass in the pending status to pick out only the
    # pending reimbursement requests.
    def view_pending_emp_reimbursements(self, employee_id: int):
        employee = self.find_employee_per_id(employee_id)
        if employee:
            sql = "select * from reimbursement where employee_id = %s and status = 'Pending'"
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            reimburse_records = cursor.fetchall()
            pending_reimbursements_list = []
            # We've found all the pending reimbursements for this particular employee and appended them to their own
            # list.
            for pending in reimburse_records:
                pending_reimbursements_list.append(Reimbursement(*pending))
            # Now we're returning that list of pending reimbursements to the front-end website.
            return pending_reimbursements_list
        else:
            return False



    # This method handles populating the reimbursement requests, per employee, that have been approved.
    def view_approved_emp_reimbursements(self, employee_id: int, approved: str):
        employee = self.find_employee_per_id(employee_id)
        if employee:
            sql = 'select * from reimbursement where employee_id = %s and status = %s'
            cursor = connection.cursor()
            cursor.execute(sql, (employee_id, approved))
            reimburse_records = cursor.fetchall()
            approved_reimbursements_list = []
            # We've found all the approved reimbursements for this particular employee and appended them to their own
            # list.
            for approved in reimburse_records:
                approved_reimbursements_list.append(Reimbursement(*approved))
            # Now we're returning that list of approved reimbursements to the front-end website.
            return approved_reimbursements_list
        else:
            return False



    # This method handles populating the reimbursement requests, per employee, that were denied.
    def view_denied_emp_reimbursements(self, employee_id: int, denied: str):
        employee = self.find_employee_per_id(employee_id)
        if employee:
            sql = 'select * from reimbursement where employee_id = %s and status = %s'
            cursor = connection.cursor()
            cursor.execute(sql, (employee_id, denied))
            reimburse_records = cursor.fetchall()
            denied_reimbursements_list = []
            # We've found all the denied reimbursements for this particular employee and appended them to their own
            # list.
            for denied in reimburse_records:
                denied_reimbursements_list.append(Reimbursement(*denied))
            # Now we're returning that list of denied reimbursements to the front-end website.
            return denied_reimbursements_list
        else:
            return False

