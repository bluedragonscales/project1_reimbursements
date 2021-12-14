from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class ManagerService(ABC):

    @abstractmethod
    def service_login(self):
        pass

    @abstractmethod
    def service_approve_reimbursement(self, reimburse_id: int):
        pass

    @abstractmethod
    def service_deny_reimbursement(self, reimburse_id: int):
        pass

    @abstractmethod
    def service_view_all_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_pending_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_approved_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def service_view_denied_requests(self) -> list[Reimbursement]:
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