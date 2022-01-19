from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.custom_exceptions import *
from service_layer.postgres_manager_service import PostgresManagerService

manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)


# SERVICE LOGIN TESTS
def test_validate_manager_cant_login_with_incorrect_credentials():
    try:
        manager_service.service_manager_login('agentscarn', 'office123')
        assert False
    except CredentialsFalseException as c:
        assert str(c) == "The username or password is incorrect!"


def test_validate_manager_cant_login_with_spaces():
    try:
        manager_service.service_manager_login('Cornell Man', 'capella')
        assert False
    except SpacesException as s:
        assert str(s) == "Spaces are not allowed in username or password."



# APPROVE REQUEST TEST
def test_validate_request_already_approved():
    try:
        manager_service.service_approve_reimbursement(16, 'Oops, test did not do as intended')
        assert False
    except NoLongerPendingException as n:
        assert str(n) == "This reimbursement was already approved or denied!"



# DENY REQUEST TEST
def test_validate_request_already_denied():
    try:
        manager_service.service_deny_reimbursement(21, 'Oops, test did not do as intended')
        assert False
    except NoLongerPendingException as n:
        assert str(n) == "This reimbursement was already approved or denied!"



# REIMBURSEMENTS PER EMPLOYEE TEST
def test_validate_employee_doesnt_exist_so_cant_get_requests():
    try:
        manager_service.service_all_reimbursements_per_employee(200)
        assert False
    except NonExistentEmployeeException as e:
        assert str(e) == "This employee does not exist!"