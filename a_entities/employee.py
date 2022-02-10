
# EMPLOYEE ENTITY
class Employee:
    def __init__(self, employee_id: int, manager_id: int, full_name: str, username: str, password: str):
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.full_name = full_name
        self.username = username
        self.password = password


    def employee_dictionary(self):
        return {
            "employeeId" : self.employee_id,
            "managerId" : self.manager_id,
            "fullName" : self.full_name,
            "username" : self.username,
            "password" : self.password
        }
