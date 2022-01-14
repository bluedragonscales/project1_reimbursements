# Project 1 is to create a fictional or fantasy company with a reimbursement system. The employees can request a
# reimbursement for any money they spent out of their own pocket for the company. The managers can approve or deny their
# requests depending on whether the requests are legitimate or not.

# The employees and managers were created directly in the database, so I've made the reimbursements into an entity that
# the employees and managers can interact with.

class Reimbursement:
    def __init__(self, reimburse_id: int, employee_id: int, amount: float, status: str, emp_reason: str, manager_reason: str):
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
