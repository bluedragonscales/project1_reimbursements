from dao_layer.postgres_manager_dao import PostgresManagerDAO


manager_dao = PostgresManagerDAO()


# MANAGER LOGIN TESTS
def test_manager_login_happy():
    # If all credentials are correct.
    manager_login = manager_dao.manager_login('CornellMan', 'acapella')
    assert manager_login

def test_manager_login_wrong_password_sad():
    # If the password is wrong.
    manager_login = manager_dao.manager_login('CornellMan', 'acapela')
    assert manager_login == False

def test_manager_login_wrong_username_sad():
    # If the username is wrong.
    manager_login = manager_dao.manager_login('AgentScarn', 'office1234')
    assert manager_login == False



# VIEW PENDING REIMBURSEMENTS TESTS
def test_view_pending_reimbursements_happy():
    # If there is at least one pending request.
    pending_list = manager_dao.all_pending_reimbursements()
    assert len(pending_list) > 1

def test_view_pending_reimbursements_sad():
    # If there are no pending requests.
    pending_list = manager_dao.all_pending_reimbursements()
    assert pending_list == False




# APPROVE REIMBURSEMENT TESTS
def test_approve_reimbursement_happy():
    # If the reimbursement request is NOT already approved or denied.
    approved = manager_dao.approve_reimbursement(22, 'It better be the good kind.')
    assert approved == 'Approved'

def test_approve_reimbursement_sad():
    # If the reimbursement request IS already approved or denied.
    cant_approve = manager_dao.approve_reimbursement(3, 'Test is not working.')
    assert cant_approve is None



# DENY REIMBURSEMENT TESTS
def test_deny_reimbursement_happy():
    # If the reimbursement request is NOT already approved or denied.
    denied = manager_dao.deny_reimbursement(24, "We never got any. What is that stain?")
    assert denied == 'Denied'

def test_deny_reimbursement_sad():
    # If the reimbursement request IS already approved or denied.
    denied = manager_dao.deny_reimbursement(2, "Test did not work")
    assert denied is None



# VIEW APPROVED REIMBURSEMENTS TESTS
def test_view_approved_requests_happy():
    # If there is at least one approved request.
    approved_list = manager_dao.view_approved_requests()
    assert len(approved_list) > 0

def test_view_approved_requests_sad():
    # If there are no approved requests.
    approved_list = manager_dao.view_approved_requests()
    assert approved_list == False


# VIEW DENIED REIMBURSEMENTS TESTS
def test_view_denied_requests_happy():
    # If there is at least one denied request.
    denied_list = manager_dao.view_denied_requests()
    assert len(denied_list) > 0

def test_view_denied_requests_sad():
    # If there are no denied requests.
    denied_list = manager_dao.view_denied_requests()
    assert denied_list == False



# VIEW REIMBURSEMENTS PER EMPLOYEE TESTS
def test_all_reimbursements_per_employee_happy():
    # If this employee has at least one reimbursement request.
    emp_reimburse_list = manager_dao.all_reimbursements_per_employee(4)
    assert len(emp_reimburse_list) > 0

def test_all_reimbursements_per_employee_sad():
    # If this employee has no reimbursement requests.
    emp_reimburse_list = manager_dao.all_reimbursements_per_employee(6)
    assert emp_reimburse_list == False



# VIEW ALL EMPLOYEES TEST
def test_view_all_employees_happy():
    # If there are at least 6 employees.
    employee_list = manager_dao.view_all_employees()
    assert len(employee_list) > 5



# STATISTICS TESTS
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