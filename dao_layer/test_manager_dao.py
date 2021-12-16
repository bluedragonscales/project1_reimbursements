from dao_layer.postgres_manager_dao import PostgresManagerDAO

manager_dao = PostgresManagerDAO()



def test_login():
    credentials = manager_dao.manager_login(2)
    assert credentials[1] == ""



def test_approve_deny_reimbursement_happy():
    approve_status = manager_dao.approve_deny_reimbursement(2, "Approved")
    assert approve_status == "Approved"



def test_view_all_reimbursement_requests_happy():
    all_reimbursements = manager_dao.view_all_reimbursement_requests()
    assert len(all_reimbursements) > 0



def test_view_reimburse_requests_per_status_happy():
    pending_reimbursements = manager_dao.view_reimburse_requests_per_status("Denied")
    assert len(pending_reimbursements) >= 0



def test_view_statistics():
    pass
