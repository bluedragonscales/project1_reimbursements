from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO
from database_connection import connection


class PostgresEmployeeDAO(EmployeeDAO):
    reimbursement_pending_list = []


    def login(self, employee_id: int):
        pass



    def submit_reimbursement(self, employee_id: int, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "project1".reimbursement values(default, %s, %s, %s, "Pending") returning reimburse_id'
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, reimbursement.request_label, reimbursement.amount))
        reimburse_id = cursor.fetchone()[0]
        reimbursement.reimburse_id = reimburse_id
        PostgresEmployeeDAO.reimbursement_pending_list.append(reimbursement.reimburse_id)
        return reimbursement



    def view_reimbursement_per_employee(self, employee_id: int) -> list[Reimbursement]:
        sql = 'select * from "project1".reimbursement where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        reimburse_records = cursor.fetchall()
        reimburse_list_per_employee = []
        for reimburse in reimburse_records:
            reimburse_list_per_employee.append(Reimbursement(*reimburse))
        return reimburse_list_per_employee



    def view_reimbursement_status(self, reimburse_id: int):
        sql = 'select approved from "project1".reimbursement where reimburse_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [reimburse_id])
        status = cursor.fetchone()[0]
        if not status:
            return "This reimbursement is pending approval."
        else:
            return "This reimbursement has been approved."



    def logout(self, employee_id):
        pass