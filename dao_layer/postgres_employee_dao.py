from a_entities.reimbursement import Reimbursement
from dao_layer.abstract_employee_dao import EmployeeDAO
from database_connection import connection


class PostgresEmployeeDAO(EmployeeDAO):

    def login(self, employee_id: int):
        pass



    def submit_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "project1".reimbursement values(default, %s, %s, %s, %s) returning reimburse_id'
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.employee_id,
                             reimbursement.request_label,
                             reimbursement.amount,
                             reimbursement.status))
        reimburse_id = cursor.fetchone()[0]
        reimbursement.reimburse_id = reimburse_id
        connection.commit()
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



    def logout(self, employee_id):
        pass