from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class ManagerService(ABC):

    @abstractmethod
    def service_login(self):
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
    def service_view_statistics(self):
        pass
    # View highest reimbursement request.
    # View lowest reimbursement request.
    # View total reimbursement value.
    # View how much reimbursement each employee has asked for.
    # View how much reimbursement has been approved.

    @abstractmethod
    def service_logout(self):
        pass