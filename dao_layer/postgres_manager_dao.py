from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):

    def manager_login(self, manager_id: int, password: str):
        sql = 'select password from "project1".manager where manager_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        validate = cursor.fetchone()[0]
        if validate == password:
            return True
        else:
            return False


    def approve_deny_reimbursement(self, reimburse_id: int, status: str):
        sql = 'update "project1".reimbursement set status = %s where reimburse_id = %s returning status'
        cursor = connection.cursor()
        cursor.execute(sql, (status, reimburse_id))
        status = cursor.fetchone()[0]
        connection.commit()
        return status



    def view_all_reimbursement_requests(self) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement'
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimburse in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimburse))
        return reimbursement_list



    def view_reimburse_requests_per_status(self, status: str) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where status = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [status])
        reimburse_records = cursor.fetchall()
        reimburse_list = []
        for reimburse in reimburse_records:
            reimburse_list.append(Reimbursement(*reimburse))
        return reimburse_list



    def view_statistics(self, statistic: str):
        cursor = connection.cursor()
        if statistic == "Highest":    # To view the highest reimbursement request.
            sql_high = 'select max(amount) from "project1".reimbursement'
            cursor.execute(sql_high)
            highest_reimbursement = cursor.fetchone()[0]
            return highest_reimbursement
        elif statistic == "Lowest":  # To view the lowest reimbursement request.
            sql_low = 'select min(amount) from "project1".reimbursement'
            cursor.execute(sql_low)
            lowest_reimbursement = cursor.fetchone()[0]
            return lowest_reimbursement
        elif statistic == "Average":   # To view the average of the reimbursement amounts that were approved.
            sql_avg = 'select avg(amount) from "project1".reimbursement = Approved'
            cursor.execute(sql_avg)
            average = cursor.fetchone()[0]
            return average
        elif statistic == "Total":   # To view the total amount of reimbursements.
            sql_total = 'select sum(amount) from "project1".reimbursement where status = Approved'
            cursor.execute(sql_total)
            total = cursor.fetchone()[0]
            return total
        elif statistic == "Count":   # To view how many reimbursements have been requested no matter the status.
            sql_count = 'select count(amount) from "project1".reimbursement'
            cursor.execute(sql_count)
            count = cursor.fetchone()[0]
            return count
