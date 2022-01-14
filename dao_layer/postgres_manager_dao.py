from a_entities.employee import Employee
from a_entities.manager import Manager
from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):

    def manager_login(self, manager_username: str, manager_password: str):
        sql = 'select * from manager where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [manager_username])
        manager_record = cursor.fetchone()
        if manager_record:
            manager = Manager(*manager_record)
            if manager.username == manager_username and manager.password == manager_password:
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
        if len(pending_list) > 0:
            return pending_list
        else:
            return False



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
        if len(approved_list) > 0:
            return approved_list
        else:
            return False



    def view_denied_requests(self):
        sql = "select * from reimbursement where status = 'Denied'"
        cursor = connection.cursor()
        cursor.execute(sql)
        denied_reimbursements = cursor.fetchall()
        denied_list = []
        for reimburse in denied_reimbursements:
            denied_list.append(Reimbursement(*reimburse))
        if len(denied_list) > 0:
            return denied_list
        else:
            return False



    def all_reimbursements_per_employee(self, emp_id: int):
        sql = "select * from reimbursement where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        employee_reimbursements = cursor.fetchall()
        emp_reimburse_list = []
        for emp_reimburse in employee_reimbursements:
            emp_reimburse_list.append(Reimbursement(*emp_reimburse))
        if len(emp_reimburse_list) > 0:
            return emp_reimburse_list
        else:
            return False



    def view_all_employees(self) -> list[Employee]:
        sql = "select * from employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        employees = cursor.fetchall()
        employee_list = []
        for employee in employees:
            employee_list.append(Employee(*employee))
        return employee_list




    # To show which employee has requested the highest dollar amount in reimbursements.
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



    # Will be used to show which employee has made the most reimbursement requests.
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








    # def view_all_reimbursement_requests(self) -> list[Reimbursement]:
    #     sql = 'select * from "project1".reimbursement'
    #     cursor = connection.cursor()
    #     cursor.execute(sql)
    #     reimbursement_records = cursor.fetchall()
    #     reimbursement_list = []
    #     for reimburse in reimbursement_records:
    #         reimbursement_list.append(Reimbursement(*reimburse))
    #     return reimbursement_list
    #
    #
    #
    # def view_reimburse_requests_per_status(self, status: str) -> list[Reimbursement]:
    #     sql = 'select * from "project1".reimbursement where status = %s'
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [status])
    #     reimburse_records = cursor.fetchall()
    #     reimburse_list = []
    #     for reimburse in reimburse_records:
    #         reimburse_list.append(Reimbursement(*reimburse))
    #     return reimburse_list
    #
    #
    #
    # def view_statistics(self, statistic: str):
    #     cursor = connection.cursor()
    #     if statistic == "Highest":    # To view the highest reimbursement request.
    #         sql_high = 'select max(amount) from "project1".reimbursement'
    #         cursor.execute(sql_high)
    #         highest_reimbursement = cursor.fetchone()[0]
    #         return highest_reimbursement
    #     elif statistic == "Lowest":  # To view the lowest reimbursement request.
    #         sql_low = 'select min(amount) from "project1".reimbursement'
    #         cursor.execute(sql_low)
    #         lowest_reimbursement = cursor.fetchone()[0]
    #         return lowest_reimbursement
    #     elif statistic == "Average":   # To view the average of the reimbursement amounts that were approved.
    #         sql_avg = 'select avg(amount) from "project1".reimbursement'
    #         cursor.execute(sql_avg)
    #         average = cursor.fetchone()[0]
    #         return average
    #     elif statistic == "Total":   # To view the total amount of reimbursements.
    #         sql_total = 'select sum(amount) from "project1".reimbursement'
    #         cursor.execute(sql_total)
    #         total = cursor.fetchone()[0]
    #         return total
    #     elif statistic == "Count":   # To view how many reimbursements have been requested no matter the status.
    #         sql_count = 'select count(amount) from "project1".reimbursement'
    #         cursor.execute(sql_count)
    #         count = cursor.fetchone()[0]
    #         return count
