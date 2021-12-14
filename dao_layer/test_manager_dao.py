from dao_layer.postgres_manager_dao import PostgresManagerDAO

manager_dao = PostgresManagerDAO()



def test_login():
    pass



def test_approve_reimbursement():
    approve_status = manager_dao.approve_reimbursement(1)
    assert approve_status == "Approved"



def test_deny_reimbursement():
    deny_status = manager_dao.deny_reimbursement(2)
    assert deny_status == "Denied"



def test_view_all_reimbursement_requests():
    all_reimbursements = manager_dao.view_all_reimbursement_requests()
    assert all_reimbursements > 0



def test_view_pending_reimbursement_requests():
    pending_reimbursements = manager_dao.view_pending_reimbursement_requests()
    assert pending_reimbursements > 0



def test_view_approved_requests():
    approved_reimbursements = manager_dao.view_approved_requests()
    assert approved_reimbursements > 0



def test_view_denied_requests():
    denied_reimbursements = manager_dao.view_denied_requests()
    assert denied_reimbursements > 0



def test_view_statistics():
    pass



def test_logout():
    pass
