from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):

    def login(self):
        pass


    def approve_reimbursement(self, reimburse_id: int):
        sql = 'update "project1".reimbursement set status = "Approved" where reimburse_id = %s returning status'
        cursor = connection.cursor()
        cursor.execute(sql, [reimburse_id])
        status = cursor.fetchone()[0]
        connection.commit()
        return status



    def deny_reimbursement(self, reimburse_id: int):
        sql = 'update "project1".reimbursement set status = "Denied" where reimburse_id = %s returning status'
        cursor = connection.cursor()
        cursor.execute(sql, [reimburse_id])
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



    def view_pending_reimbursement_requests(self) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where status = "Pending"'
        cursor = connection.cursor()
        cursor.execute(sql)
        pending_records = cursor.fetchall()
        pending_list = []
        for reimburse in pending_records:
            pending_list.append(Reimbursement(*reimburse))
        return pending_list



    def view_approved_requests(self) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where status = "Approved"'
        cursor = connection.cursor()
        cursor.execute(sql)
        approved_records = cursor.fetchall()
        approved_list = []
        for reimburse in approved_records:
            approved_list.append(Reimbursement(*reimburse))
        return approved_list



    def view_denied_requests(self) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where status = "Denied"'
        cursor = connection.cursor()
        cursor.execute(sql)
        denied_records = cursor.fetchall()
        denied_list = []
        for reimburse in denied_records:
            denied_list.append(Reimbursement(*reimburse))
        return denied_list



    def view_statistics(self):
        pass



    def logout(self):
        pass