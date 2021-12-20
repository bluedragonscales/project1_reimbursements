from dao_layer.postgres_manager_dao import PostgresManagerDAO

manager_dao = PostgresManagerDAO()



def test_login():
    valid_login = manager_dao.manager_login(2, "acapella")
    assert valid_login



def test_approve_deny_reimbursement_happy():
    approve_status = manager_dao.approve_deny_reimbursement(3, "Denied")
    assert approve_status == "Denied"



def test_view_all_reimbursement_requests_happy():
    all_reimbursements = manager_dao.view_all_reimbursement_requests()
    assert len(all_reimbursements) > 0



def test_view_reimburse_requests_per_status_happy():
    pending_reimbursements = manager_dao.view_reimburse_requests_per_status("Denied")
    assert len(pending_reimbursements) >= 0



def test_view_statistics():
    count_reimbursements = manager_dao.view_statistics("Count")
    assert count_reimbursements == 4
