from flask import Flask, request, jsonify
from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.postgres_employee_service import PostgresEmployeeService
from service_layer.postgres_manager_service import PostgresManagerService
from service_layer.custom_exceptions import *
import logging
from flask_cors import CORS

# LOGGING CONFIGURATION
logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

# FLASK AND CORS OBJECTS
app = Flask(__name__)
CORS(app)

# CLASS OBJECTS FOR INJECTION AND METHOD USE
employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)
manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)



# ROUTES FOR THE EMPLOYEE SIDE
@app.post("/employee/login")
def employee_login():
    try:
        login_body = request.get_json()
        username = login_body['username']
        password = login_body['password']
        employee = employee_service.service_employee_login(username, password)
        employee_as_dictionary = employee.employee_dictionary()
        return jsonify(employee_as_dictionary), 201
    except SpacesException as s:
        exception_dictionary = {"Message": str(s)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404
    except CredentialsFalseException as c:
        exception_dictionary = {"Message": str(c)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404



@app.post("/employee/reimbursement")
def submit_new_reimbursement():
    try:
        rb_data = request.get_json()
        new_reimbursement = Reimbursement(int(rb_data["reimburseId"]),
                                          int(rb_data["employeeId"]),
                                          float(rb_data["amount"]),
                                          rb_data["status"],
                                          rb_data["empReason"],
                                          rb_data["managerReason"])
        rb_to_return = employee_service.service_submit_new_reimbursement(new_reimbursement)
        rb_as_dictionary = rb_to_return.reimbursement_dictionary()
        return jsonify(rb_as_dictionary), 201
    except InvalidAmountException as i:
        exception_dictionary = {"Message": str(i)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404
    except NonExistentEmployeeException as e:
        exception_dictionary = {"Message": str(e)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404




@app.get("/employee/pending/<employee_id>")
def view_pending_emp_reimbursements(employee_id: str):
    rb_pending_results = employee_service.service_view_pending_emp_reimbursements(int(employee_id))
    pending_results_as_dictionary = []
    for rb in rb_pending_results:
        dictionary_of_pending = rb.reimbursement_dictionary()
        pending_results_as_dictionary.append(dictionary_of_pending)
    return jsonify(pending_results_as_dictionary), 200



@app.get("/employee/approved/<employee_id>")
def view_approved_emp_reimbursements(employee_id: str):
    rb_approved_results = employee_service.service_view_approved_emp_reimbursements(int(employee_id))
    approved_results_as_dictionary = []
    for rb in rb_approved_results:
        dictionary_of_approvals = rb.reimbursement_dictionary()
        approved_results_as_dictionary.append(dictionary_of_approvals)
    return jsonify(approved_results_as_dictionary), 200



@app.get("/employee/denied/<employee_id>")
def view_denied_emp_reimbursements(employee_id: str):
    rb_denied_results = employee_service.service_view_denied_emp_reimbursements(int(employee_id))
    denied_results_as_dictionary = []
    for rb in rb_denied_results:
        dictionary_of_denied = rb.reimbursement_dictionary()
        denied_results_as_dictionary.append(dictionary_of_denied)
    return jsonify(denied_results_as_dictionary), 200







# ROUTES FOR THE MANAGER SIDE
@app.post("/manager/login")
def manager_login():
    try:
        login_body = request.get_json()
        username = login_body['username']
        password = login_body['password']
        manager = manager_service.service_manager_login(username, password)
        manager_as_dictionary = manager.manager_dictionary()
        return jsonify(manager_as_dictionary), 201
    except SpacesException as s:
        exception_dictionary = {"Message": str(s)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404
    except CredentialsFalseException as c:
        exception_dictionary = {"Message": str(c)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404




@app.get("/manager/pendingList")
def view_all_pending_reimbursements():
    pending_list = manager_service.service_all_pending_reimbursements()
    pending_as_dictionaries = []
    for pend in pending_list:
        dictionary_pending_list = pend.reimbursement_dictionary()
        pending_as_dictionaries.append(dictionary_pending_list)
    return jsonify(pending_as_dictionaries), 200




@app.patch("/manager/approve")
def approve_reimbursement():
    try:
        request_data = request.get_json()
        r_id = request_data['reimburseId']
        m_reason = request_data['reason']
        approval = manager_service.service_approve_reimbursement(int(r_id), m_reason)
        return jsonify(approval), 200
    except NoLongerPendingException as n:
        exception_dictionary = {"Message": str(n)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404




@app.patch("/manager/deny")
def deny_reimbursement():
    try:
        request_data = request.get_json()
        r_id = request_data['reimburseId']
        m_reason = request_data['reason']
        denial = manager_service.service_deny_reimbursement(int(r_id), m_reason)
        return jsonify(denial), 200
    except NoLongerPendingException as n:
        exception_dictionary = {"Message": str(n)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404





@app.get("/manager/approvals")
def view_all_reimbursement_approvals():
    all_approvals = manager_service.service_view_approved_requests()
    approved_as_dictionaries = []
    for appr in all_approvals:
        dictionary_approvals = appr.reimbursement_dictionary()
        approved_as_dictionaries.append(dictionary_approvals)
    return jsonify(approved_as_dictionaries), 200




@app.get("/manager/denials")
def view_all_reimbursement_denials():
    all_denials = manager_service.service_view_denied_requests()
    denied_as_dictionaries = []
    for deny in all_denials:
        dictionary_denials = deny.reimbursement_dictionary()
        denied_as_dictionaries.append(dictionary_denials)
    return jsonify(denied_as_dictionaries), 200




@app.get("/manager/reimbursePerEmp")
def view_reimbursements_per_employee():
    try:
        request_data = request.get_json()
        emp_id = request_data['employeeId']
        emp_reimburse_list = manager_service.service_all_reimbursements_per_employee(int(emp_id))
        emp_reimburse_as_dict = []
        for emp_reim in emp_reimburse_list:
            dictionary_reimbursements = emp_reim.reimbursement_dictionary()
            emp_reimburse_as_dict.append(dictionary_reimbursements)
        return jsonify(emp_reimburse_as_dict), 200
    except NonExistentEmployeeException as n:
        exception_dictionary = {"Message": str(n)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception, 404





# Routes for statistics managers can look at.
@app.get("/manager/highestReimburseTotal")
def view_highest_reimbursement_amount():
    data_tuple = manager_service.service_highest_reimbursement_total()
    highest_sum = data_tuple[0]
    emp = data_tuple[1]
    emp_name = employee_service.service_find_employee_per_id(emp)
    stat_dictionary = {"employeeName": emp_name.full_name, "reimbursementTotal": highest_sum}
    return jsonify(stat_dictionary), 200


@app.get("/manager/mostReimburseRequests")
def view_who_has_most_reimburse_requests():
    data_tuple = manager_service.service_all_requests_per_employee()
    most_requests = data_tuple[0]
    emp = data_tuple[1]
    emp_name = employee_service.service_find_employee_per_id(emp)
    stat_dictionary = {"employeeName": emp_name.full_name, "amountOfRequests": most_requests}
    return jsonify(stat_dictionary), 200


@app.get("/manager/dollarTotalOfApprovals")
def dollar_total_of_approved_reimbursements():
    dollar_total = manager_service.service_dollar_total_of_approved_reimbursements()
    stat_dictionary = {"dollarTotalApproved": dollar_total}
    return jsonify(stat_dictionary), 200


@app.get("/manager/employeeMostDenials")
def employee_with_most_denials():
    data_tuple = manager_service.service_employee_with_most_denials()
    most_denials = data_tuple[0]
    emp = data_tuple[1]
    emp_name = employee_service.service_find_employee_per_id(emp)
    stat_dictionary = {"employeeName": emp_name.full_name, "amountOfDenials": most_denials}
    return jsonify(stat_dictionary), 200


@app.get("/manager/employeeMostApprovals")
def employee_with_most_approvals():
    data_tuple = manager_service.service_employee_with_most_approvals()
    most_approvals = data_tuple[0]
    emp = data_tuple[1]
    emp_name = employee_service.service_find_employee_per_id(emp)
    stat_dictionary = {"employeeName": emp_name.full_name, "amountOfApprovals": most_approvals}
    return jsonify(stat_dictionary), 200




app.run()