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


    def all_pending_reimbursements(self) -> list[Reimbursement]:
        sql = "select * from reimbursement where status = 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql)
        pending_reimbursements = cursor.fetchall()
        pending_list = []
        for reimburse in pending_reimbursements:
            pending_list.append(Reimbursement(*reimburse))
        return pending_list


    def approve_reimbursement(self, reimburse_id: int, message: str):
        sql = "update reimbursement set status = 'Approved', manager_reason = %s where reimburse_id = %s" \
              " and status = 'Pending'"
        cursor = connection.cursor()
        cursor.execute(sql, (message, reimburse_id))
        status = cursor.fetchone()[0]
        connection.commit()
        if status == "Approved":
            return status
        else:
            return False



    def deny_reimbursement(self, reimburse_id: int, message: str):
        still_pending = self.all_pending_reimbursements()
        for pr in still_pending:
            if pr.reimburse_id == reimburse_id:
                sql = "update reimbursement set status = 'Denied', manager_reason = %s where reimburse_id = %s " \
                      "returning status"
                cursor = connection.cursor()
                cursor.execute(sql, [reimburse_id])
                status = cursor.fetchone()[0]
                connection.commit()
                return status
            else:
                return False


    def view_past_approved_requests(self) -> list[Reimbursement]:
        pass

    # Be able to view all past denied reimbursement requests.
    def view_past_denied_requests(self) -> list[Reimbursement]:
        pass

    # To show which employee has requested the highest dollar total in reimbursements.
    def employee_with_highest_total(self):
        pass

    # To show which employee has made the most reimbursement requests.
    def employee_with_most_requests(self):
        pass

    # To show the total dollar amount of all reimbursements approved.
    def dollar_total_of_approved_reimbursements(self):
        pass

    # To show which employee has the most denials.
    def employee_with_most_denials(self):
        pass

    # To show which employee has the most approvals.
    def employee_with_most_approvals(self):
        pass








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
