from abc import ABC, abstractmethod
from a_entities.reimbursement import Reimbursement


class ManagerService(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def approve_reimbursement(self, reimburse_id: int):
        pass

    @abstractmethod
    def deny_reimbursement(self, reimburse_id: int):
        pass

    @abstractmethod
    def view_all_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_pending_reimbursement_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_approved_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_denied_requests(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def view_statistics(self):
        pass
    # View highest reimbursement request.
    # View lowest reimbursement request.
    # View total reimbursement value.
    # View how much reimbursement each employee has asked for.
    # View how much reimbursement has been approved.

    @abstractmethod
    def logout(self):
        pass