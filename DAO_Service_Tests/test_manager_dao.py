from dao_layer.postgres_manager_dao import PostgresManagerDAO


manager_dao = PostgresManagerDAO()


# MANAGER LOGIN TESTS
def test_manager_login_happy():
    manager_login = manager_dao.manager_login('CornellMan', 'acapella')
    assert manager_login

def test_manager_login_wrong_password_sad():
    manager_login = manager_dao.manager_login('CornellMan', 'acapela')
    assert manager_login == False

def test_manager_login_wrong_username_sad():
    manager_login = manager_dao.manager_login('AgentScarn', 'office1234')
    assert manager_login == False



# VIEW PENDING REIMBURSEMENTS TESTS
def test_view_pending_reimbursements_happy():
    pending_list = manager_dao.all_pending_reimbursements()
    assert len(pending_list) > 1

def test_view_pending_reimbursements_sad():
    pending_list = manager_dao.all_pending_reimbursements()
    assert pending_list == False




# APPROVE REIMBURSEMENT TESTS
def test_approve_reimbursement_happy():
    approved = manager_dao.approve_reimbursement(22, 'It better be the good kind.')
    assert approved == 'Approved'

def test_approve_reimbursement_sad():
    cant_approve = manager_dao.approve_reimbursement(3, 'Test is not working.')
    assert cant_approve is None



# DENY REIMBURSEMENT TESTS
def test_deny_reimbursement_happy():
    denied = manager_dao.deny_reimbursement(24, "We never got any. What is that stain?")
    assert denied == 'Denied'

def test_deny_reimbursement_sad():
    denied = manager_dao.deny_reimbursement(2, "Test did not work")
    assert denied is None



# VIEW APPROVED REIMBURSEMENTS TESTS
def test_view_approved_requests_happy():
    approved_list = manager_dao.view_approved_requests()
    assert len(approved_list) >= 1

def test_view_approved_requests_sad():
    approved_list = manager_dao.view_approved_requests()
    assert approved_list == False


# VIEW DENIED REIMBURSEMENTS TESTS
def test_view_denied_requests_happy():
    denied_list = manager_dao.view_denied_requests()
    assert len(denied_list) >= 1

def test_view_denied_requests_sad():
    denied_list = manager_dao.view_denied_requests()
    assert denied_list == False



# VIEW REIMBURSEMENTS PER EMPLOYEE TESTS
def test_all_reimbursements_per_employee_happy():
    emp_reimburse_list = manager_dao.all_reimbursements_per_employee(4)
    assert len(emp_reimburse_list) >= 1

def test_all_reimbursements_per_employee_sad():
    emp_reimburse_list = manager_dao.all_reimbursements_per_employee(6)
    assert emp_reimburse_list == False



# VIEW ALL EMPLOYEES TEST
def test_view_all_employees_happy():
    employee_list = manager_dao.view_all_employees()
    assert len(employee_list) >= 6



# STATISTICS PER EMPLOYEE TESTS
def test_highest_reimbursement_total_happy():
    sum = manager_dao.highest_reimbursement_total()
    assert sum[0] == 1668.24 and sum[1] == 6

def test_all_requests_per_employee_happy():
    all_requests = manager_dao.all_requests_per_employee()
    assert all_requests[0] == 6 and all_requests[1] == 4

def test_dollar_total_of_approved_reimbursements_happy():
    sum_approved = manager_dao.dollar_total_of_approved_reimbursements()
    assert sum_approved >= 1579.09

def test_employee_with_most_denials_happy():
    count_denials = manager_dao.employee_with_most_denials()
    assert count_denials[0] == 3 and count_denials[1] == 4

def test_employee_with_most_approvals_happy():
    count_approvals = manager_dao.employee_with_most_approvals()
    assert count_approvals[0] == 3 and count_approvals[1] == 1