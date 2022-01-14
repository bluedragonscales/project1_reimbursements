
# MANAGER ENTITY
class Manager:
    def __init__(self, manager_id: int, full_name: str, username: str, password: str):
        self.manager_id = manager_id
        self.full_name = full_name
        self.username = username
        self.password = password


    def reimbursement_dictionary(self):
        return {
            "managerId" : self.manager_id,
            "fullName" : self.full_name,
            "username" : self.username,
            "password" : self.password
        }