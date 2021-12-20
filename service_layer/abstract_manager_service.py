from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class ManagerService(ABC):

    @abstractmethod
    def service_manager_login(self, manager_id: int, password: str):
        pass

    @abstractmethod
    def service_approve_deny_reimbursement(self, reimburse_id: int, status: str):
        pass

    @abstractmethod
    def service_view_all_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_reimburse_requests_per_status(self, status: str) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_statistics(self, statistic: str):
        pass