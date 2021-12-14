from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.postgres_manager_service import PostgresManagerService

manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)


def test_login():
    pass
    # Test to make sure correct login credentials are entered.



def test_view_statistics():
    pass