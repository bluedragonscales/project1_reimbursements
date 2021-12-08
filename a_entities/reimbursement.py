# Create reimbursements for employees. Employees will be logged and THEN their reimbursement requests
# will be accepted or denied.

# What would be the main entity for these employee reimbursement request scenarios?
# An employee object could have a method to store reimbursement requests.
# If the employee is already created as a table in postgres, then we could create just a reimbursement
# object.


class Reimbursement:
    def __init__(self, reimburse_id: int, employee_id: int, request_label: str, amount: float, approved: bool):
        self.reimburse_id = reimburse_id
        self.employee_id = employee_id
        self.request_label = request_label
        self.amount = amount
        self.approved = approved

    def reimbursement_dictionary(self):
        return {
            "reimburseId" : self.reimburse_id,
            "employeeId" : self.employee_id,
            "requestLabel" : self.request_label,
            "amount" : self.amount,
            "approved" : self.approved
        }
