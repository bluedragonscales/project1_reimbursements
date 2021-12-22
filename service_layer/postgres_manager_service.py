from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService
from service_layer.custom_exceptions import *


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao


    def service_manager_login(self, manager_id: int, password: str):
        validation = self.manager_dao.manager_login(manager_id, password)
        if validation:
            return True
        else:
            return False


    def service_approve_deny_reimbursement(self, reimburse_id: int, status: str):
        return self.manager_dao.approve_deny_reimbursement(reimburse_id, status)


    def service_view_all_reimbursement_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_all_reimbursement_requests()


    def service_view_reimburse_requests_per_status(self, status: str) -> list[Reimbursement]:
        return self.manager_dao.view_reimburse_requests_per_status(status)


    def service_view_statistics(self, statistic: str):
        return self.manager_dao.view_statistics(statistic)