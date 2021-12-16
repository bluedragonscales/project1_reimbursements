from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):

    def manager_login(self, manager_id: int):
        sql = 'select password from "project1".manager where employee_id = %s'
        sql2 = 'select username from "project1".manager where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        password = cursor.fetchone()[0]
        cursor.execute(sql2, [manager_id])
        username = cursor.fetchone()[0]
        credentials = (username, password)
        return credentials


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



    def view_statistics(self):
        pass
    # If one particular string, do that particular aggregate sql method to get the statistic.