from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.abstract_manager_service import ManagerService
from service_layer.custom_exceptions import *


class PostgresManagerService(ManagerService):

    def __init__(self, manager_dao):
        self.manager_dao: PostgresManagerDAO = manager_dao


    def service_login(self):
        pass


    def service_approve_deny_reimbursement(self, reimburse_id: int, status: str):
        reimbursement_list = self.manager_dao.view_all_reimbursement_requests()
        for rb in reimbursement_list:
            if reimburse_id == rb.reimburse_id:
                return self.manager_dao.approve_deny_reimbursement(reimburse_id, status)
            else:
                raise UnavailableException("This reimbursement request does not exist.")


    def service_view_all_reimbursement_requests(self) -> list[Reimbursement]:
        return self.manager_dao.view_all_reimbursement_requests()

    def service_view_reimburse_requests_per_status(self, status: str) -> list[Reimbursement]:
        return self.manager_dao.view_reimburse_requests_per_status(status)

    def service_view_statistics(self):
        pass

    def service_logout(self):
        pass