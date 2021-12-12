from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_manager_dao import ManagerDAO
from database_connection import connection


class PostgresManagerDAO(ManagerDAO):
    approved_reimbursement_list = []
    denied_reimbursement_list = []

    def login(self):
        pass

    def approve_reimbursement(self, reimburse_id: int):
        sql = 'update "project1".reimbursement set approved = True where reimburse_id = %s returning approved'
        cursor = connection.cursor()
        cursor.execute(sql, [reimburse_id])
        status = cursor.fetchone()[0]
        connection.commit()
        PostgresManagerDAO.approved_reimbursement_list.append(reimburse_id)
        return status



    def deny_reimbursement(self, reimburse_id: int):
        denied_list = PostgresManagerDAO.denied_reimbursement_list.append(reimburse_id)
        return denied_list
        # Instead of deleting the requests, just change the status variable to a string of
        # "denied"



    def view_all_reimbursement_requests(self) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement'
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimburse in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimburse))
        return reimbursement_list



    def view_pending_reimbursement_requests(self, reimburse_id: int) -> list[Reimbursement]:
        pass

    def view_approved_failed_requests(self, reimburse_id: int) -> list[Reimbursement]:
        pass
        # Combine both the denied and approved lists.

    def view_statistics(self):
        pass

    def logout(self):
        pass