from a_entities.employee import Employee
from a_entities.manager import Manager
from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):

    # If the username entered does not exist in the database the method will return false. If the username exists it
    # will pull up the credentials for that manager. If the password entered does not match the password for that
    # manager the method will return false. If the username and password are correct and correlated to the same manager
    # then the manager object will be returned.
    def manager_login(self, manager_username: str, manager_password: str):
        sql = 'select * from manager where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [manager_username])
        manager_record = cursor.fetchone()
        if manager_record:
            manager = Manager(*manager_record)
            if manager.password == manager_password:
                return manager
            else:
                return False
        else:
            return False




    def all_pending_reimbursements(self):
        sql = "select * from reimbursement where status = 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql)
        pending_reimbursements = cursor.fetchall()
        pending_list = []
        for reimburse in pending_reimbursements:
            pending_list.append(Reimbursement(*reimburse))
        return pending_list



    # Iterate through the pending reimbursements and if the reimburse id is found in the pending reimbursements then
    # update the reimbursement with the status approved and a message/reason from the manager. Otherwise it will return
    # with the status of None.
    def approve_reimbursement(self, reimburse_id: int, reason: str):
        pending_reimbursements = self.all_pending_reimbursements()
        for pr in pending_reimbursements:
            if pr.reimburse_id == reimburse_id:
                sql = "update reimbursement set status = 'Approved', manager_reason = %s where reimburse_id = %s " \
                          "returning status"
                cursor = connection.cursor()
                cursor.execute(sql, (reason, reimburse_id))
                status = cursor.fetchone()[0]
                connection.commit()
                return status



    # Iterate through the pending reimbursements and if the reimburse id is found in the pending reimbursements then
    # update the reimbursement with the status denied and a message/reason from the manager. Otherwise it will return
    # with the status of None.
    def deny_reimbursement(self, reimburse_id: int, reason: str):
        pending_reimbursements = self.all_pending_reimbursements()
        for pr in pending_reimbursements:
            if pr.reimburse_id == reimburse_id:
                sql = "update reimbursement set status = 'Denied', manager_reason = %s where reimburse_id = %s " \
                      "returning status"
                cursor = connection.cursor()
                cursor.execute(sql, (reason, reimburse_id))
                status = cursor.fetchone()[0]
                connection.commit()
                return status




    def view_approved_requests(self):
        sql = "select * from reimbursement where status = 'Approved'"
        cursor = connection.cursor()
        cursor.execute(sql)
        approved_reimbursements = cursor.fetchall()
        approved_list = []
        for reimburse in approved_reimbursements:
            approved_list.append(Reimbursement(*reimburse))
        return approved_list




    def view_denied_requests(self):
        sql = "select * from reimbursement where status = 'Denied'"
        cursor = connection.cursor()
        cursor.execute(sql)
        denied_reimbursements = cursor.fetchall()
        denied_list = []
        for reimburse in denied_reimbursements:
            denied_list.append(Reimbursement(*reimburse))
        return denied_list




    def view_all_employees(self) -> list[Employee]:
        sql = "select * from employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        employees = cursor.fetchall()
        employee_list = []
        for employee in employees:
            employee_list.append(Employee(*employee))
        return employee_list




    # Created a list of employees and iterating through them to make sure the inputted employee id exists, so that the
    # reimbursements for that employee can be viewed (if they have any).
    def all_reimbursements_per_employee(self, emp_id: int):
        employee_list = self.view_all_employees()
        for emp in employee_list:
            if emp.employee_id == emp_id:
                sql = "select * from reimbursement where employee_id = %s"
                cursor = connection.cursor()
                cursor.execute(sql, [emp_id])
                employee_reimbursements = cursor.fetchall()
                emp_reimburse_list = []
                for emp_reimburse in employee_reimbursements:
                    emp_reimburse_list.append(Reimbursement(*emp_reimburse))
                return emp_reimburse_list




    # Description of how this method works to get the employee that has the highest total of reimbursement requests and
    # the actual total in a tuple.
    def highest_reimbursement_total(self):
        employee_list = self.view_all_employees()
        sum_list = []
        for emp in employee_list:
            sql = "select sum(amount) from reimbursement where employee_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [emp.employee_id])
            emp_sum = cursor.fetchone()[0]
            sum_list.append(emp_sum)
            highest_sum = max(sum_list)
            max_emp = sum_list.index(highest_sum) + 1
            statistic_tuple = (highest_sum, max_emp)
        return statistic_tuple



    # To show which employee has made the most reimbursement requests.
    def all_requests_per_employee(self):
        employee_list = self.view_all_employees()
        count_list = []
        for emp in employee_list:
            sql = "select count(amount) from reimbursement where employee_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [emp.employee_id])
            emp_count = cursor.fetchone()[0]
            count_list.append(emp_count)
            highest_count = max(count_list)
            max_emp = count_list.index(highest_count) + 1
            statistic_tuple = (highest_count, max_emp)
        return statistic_tuple



    # To show the total dollar amount of all reimbursements approved.
    def dollar_total_of_approved_reimbursements(self):
        sql = "select sum(amount) from reimbursement where status = 'Approved'"
        cursor = connection.cursor()
        cursor.execute(sql)
        sum_approved = cursor.fetchone()[0]
        return sum_approved



    # To show which employee has the most denials.
    def employee_with_most_denials(self):
        employee_list = self.view_all_employees()
        denials_list = []
        for emp in employee_list:
            sql = "select count(status) from reimbursement where status = 'Denied' and employee_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [emp.employee_id])
            emp_denials = cursor.fetchone()[0]
            denials_list.append(emp_denials)
            highest_denials = max(denials_list)
            max_emp = denials_list.index(highest_denials) + 1
            statistic_tuple = (highest_denials, max_emp)
        return statistic_tuple




    # To show which employee has the most approvals.
    def employee_with_most_approvals(self):
        employee_list = self.view_all_employees()
        approvals_list = []
        for emp in employee_list:
            sql = "select count(status) from reimbursement where status = 'Approved' and employee_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [emp.employee_id])
            emp_approvals = cursor.fetchone()[0]
            approvals_list.append(emp_approvals)
            highest_approvals = max(approvals_list)
            max_emp = approvals_list.index(highest_approvals) + 1
            statistic_tuple = (highest_approvals, max_emp)
        return statistic_tuple