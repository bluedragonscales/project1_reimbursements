
# REIMBURSEMENT ENTITY
class Reimbursement:
    def __init__(self, reimburse_id: int, employee_id: int, amount: float, status: str,
                 emp_reason: str, manager_reason: str):
        self.reimburse_id = reimburse_id
        self.employee_id = employee_id
        self.amount = amount
        self.status = status
        self.emp_reason = emp_reason
        self.manager_reason = manager_reason

    def reimbursement_dictionary(self):
        return {
            "reimburseId" : self.reimburse_id,
            "employeeId" : self.employee_id,
            "amount" : self.amount,
            "status" : self.status,
            "empReason" : self.emp_reason,
            "managerReason" : self.manager_reason
        }
