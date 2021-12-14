from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao


    def service_login(self):
        pass

    def service_approve_reimbursement(self, reimburse_id: int):
        return self.manager_dao.approve_reimbursement(reimburse_id)

    def service_deny_reimbursement(self, reimburse_id: int):
        return self.manager_dao.deny_reimbursement(reimburse_id)

    def service_view_all_reimbursement_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_all_reimbursement_requests()

    def service_view_pending_reimbursement_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_pending_reimbursement_requests()

    def service_view_approved_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_approved_requests()

    def service_view_denied_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_denied_requests()

    def service_view_statistics(self):
        pass

    def service_logout(self):
        return self.manager_dao.logout()