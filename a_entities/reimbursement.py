
class Reimbursement:
    def __init__(self, reimburse_id: int, employee_id: int, request_label: str, amount: float, status: str):
        self.reimburse_id = reimburse_id
        self.employee_id = employee_id
        self.request_label = request_label
        self.amount = amount
        self.status = status

    def reimbursement_dictionary(self):
        return {
            "reimburseId" : self.reimburse_id,
            "employeeId" : self.employee_id,
            "requestLabel" : self.request_label,
            "amount" : self.amount,
            "status" : self.status
        }
