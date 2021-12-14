from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao


    def login(self):
        return self.manager_dao.login()


    def approve_reimbursement(self, reimburse_id: int):
        pass

    def deny_reimbursement(self, reimburse_id: int):
        pass

    def view_all_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    def view_pending_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    def view_approved_requests(self) -> list[Reimbursement]:
        pass

    def view_denied_requests(self) -> list[Reimbursement]:
        pass

    def view_statistics(self):
        pass

    def logout(self):
        pass