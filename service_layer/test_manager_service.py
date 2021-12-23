from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_manager_service import PostgresManagerService

manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)


def test_validate_manager_login():
    not_validated = manager_service.service_manager_login(2, "office1234")
    assert not_validated == False
