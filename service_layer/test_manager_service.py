from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_manager_service import PostgresManagerService

manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)


def test_validate_login():
    pass


def test_validate_approve_deny_reimbursement():
    try:
        manager_service.service_approve_deny_reimbursement(20, "Approved")
    except UnavailableException as u:
        assert str(u) == "This reimbursement request does not exist."


def test_validate_view_reimburse_requests_per_status():
    pass


def service_view_statistics(self):
    pass