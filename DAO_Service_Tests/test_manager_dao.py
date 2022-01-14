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
    assert len(pending_list) >= 0



# APPROVE REIMBURSEMENT TESTS
def test_approve_reimbursement_happy():
    approved = manager_dao.approve_reimbursement(5, 'You shared with the office this time.')
    assert approved == "Approved"

def test_approve_reimbursement_sad():
    cant_approve = manager_dao.approve_reimbursement(2, 'Just so long as you do not give Toby any.')
    assert cant_approve == False



# DENY REIMBURSEMENT TESTS
# def test_approve_deny_reimbursement_happy():
#     approve_status = manager_dao.approve_deny_reimbursement(3, "Denied")
#     assert approve_status == "Denied"
#
#
# def test_view_all_reimbursement_requests_happy():
#     all_reimbursements = manager_dao.view_all_reimbursement_requests()
#     assert len(all_reimbursements) > 0
#
#
#
# def test_view_reimburse_requests_per_status_happy():
#     pending_reimbursements = manager_dao.view_reimburse_requests_per_status("Denied")
#     assert len(pending_reimbursements) >= 0



# def test_view_statistics():
#     count_reimbursements = manager_dao.view_statistics("Count")
#     assert count_reimbursements > 15
