# This is the main implementation of the employee's actions with the reimbursement entity, and this is where information
# is passed back and forth through the DBeaver database management system (hosted through AWS) using PostgreSQL.

# IMPORTS
from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO
from database_connection import connection


# DAO LAYER CLASS
class PostgresEmployeeDAO(EmployeeDAO):

    # This method handles grabbing the correct password that matches the username (in this case the username is the
    # employee id). It validates as true if the correct password is used with the username, and it validates as false if
    # the incorrect password is used with the username.
    def employee_login(self, employee_id: int, password: str):
        sql = 'select password from "project1".employee where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        validate = cursor.fetchone()[0]
        # We return True or False to send back up to the API website to be able to correctly validate whether the user
        # entered the correct username and password. This makes sure the password entered on the front end, matches the
        # password pulled from the database for that employee id.
        if validate == password:
            return True
        else:
            return False




    # This method handles the creation of a new reimbursement object and stores it in the database. It takes in only
    # three initial values because the other three are default. The first default is the reimbursement id and that is a
    # serial created in PostgreSQL. The second default is the status which is initialized to pending and will be
    # modified when the manager approves or denies the reimbursement. The third default is the reason which is first
    # initialized to pending but will be changed to a reason why the manager approved or denied the reimbursement
    # request.
    def submit_new_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "project1".reimbursement values(default, %s, %s, %s, default, default) ' \
              'returning reimburse_id'
        cursor = connection.cursor()
        # The defaults don't need arguments to pass to them so we only send in the reimbursement's values that had to be
        # initialized through the employee's creation process.
        cursor.execute(sql, (reimbursement.employee_id,
                             reimbursement.request_label,
                             reimbursement.amount))
        # Since the reimbursement id is a serial created by the database, it has to be reassigned to the actual
        # reimbursement object here in Python. So we grab the value that was returned with the sql statement and then
        # assigned it to the reimbursement object.
        reimburse_id = cursor.fetchone()[0]
        reimbursement.reimburse_id = reimburse_id
        connection.commit()
        # We send the full reimbursement object back up to the API so that it can be viewed on the website.
        return reimbursement




    # This method handles populating the reimbursement requests, per employee, that are pending. We pass in the employee
    # id to pick the employee that wants to see their reimbursements. We pass in the pending status to pick out only the
    # pending reimbursement requests.
    def view_pending_emp_reimbursements(self, employee_id: int, pending: str) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where employee_id = %s and status = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, pending))
        reimburse_records = cursor.fetchall()
        pending_reimbursements_list = []
        # We've found all the pending reimbursements for this particular employee and appended them to their own list.
        for pending in reimburse_records:
            pending_reimbursements_list.append(Reimbursement(*pending))
        # Now we're returning that list of pending reimbursements to the front-end website.
        return pending_reimbursements_list



    # This method handles populating the reimbursement requests, per employee, that have been approved.
    def view_approved_emp_reimbursements(self, employee_id: int, approved: str) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where employee_id = %s and status = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, approved))
        reimburse_records = cursor.fetchall()
        approved_reimbursements_list = []
        # We've found all the approved reimbursements for this particular employee and appended them to their own list.
        for approved in reimburse_records:
            approved_reimbursements_list.append(Reimbursement(*approved))
        # Now we're returning that list of approved reimbursements to the front-end website.
        return approved_reimbursements_list



    # This method handles populating the reimbursement requests, per employee, that were denied.
    def view_denied_emp_reimbursements(self, employee_id: int, denied: str) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where employee_id = %s and status = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, denied))
        reimburse_records = cursor.fetchall()
        denied_reimbursements_list = []
        # We've found all the denied reimbursements for this particular employee and appended them to their own list.
        for denied in reimburse_records:
            denied_reimbursements_list.append(Reimbursement(*denied))
        # Now we're returning that list of denied reimbursements to the front-end website.
        return denied_reimbursements_list