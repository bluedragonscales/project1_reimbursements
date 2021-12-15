from flask import Flask, request, jsonify

from a_entities.reimbursement import Reimbursement
from dao_layer.postgres_employee_dao import PostgresEmployeeDAO
from dao_layer.postgres_manager_dao import PostgresManagerDAO
from service_layer.postgres_employee_service import PostgresEmployeeService
from service_layer.postgres_manager_service import PostgresManagerService
from service_layer.custom_exceptions import *
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
employee_dao = PostgresEmployeeDAO()
employee_service = PostgresEmployeeService(employee_dao)
manager_dao = PostgresManagerDAO()
manager_service = PostgresManagerService(manager_dao)


# These are the routes for the employee side.

# LOGIN ROUTE


@app.post("/employee/reimbursement")
def submit_reimbursement():
    try:
        rb_data = request.get_json()
        new_reimbursement = Reimbursement(rb_data["reimburseId"],
                                          rb_data["employeeId"],
                                          rb_data["requestLabel"],
                                          rb_data["amount"],
                                          rb_data["status"])
        rb_to_return = employee_service.service_submit_reimbursement(new_reimbursement)
        rb_as_dictionary = rb_to_return.reimbursement_dictionary()
        rb_as_json = jsonify(rb_as_dictionary)
        return rb_as_json
    except InvalidAmountException as a:
        exception_dictionary = {"Message": str(a)}
        jsonify_exception = jsonify(exception_dictionary)
        return jsonify_exception




@app.get("/employee/reimbursement/<employee_id>")
def view_reimbursement_per_employee(employee_id: str):
    rb_results = employee_service.service_view_reimbursement_per_employee(int(employee_id))
    results_as_dictionary = []
    for rb in rb_results:
        dictionary_rb = rb.reimbursement_dictionary()
        results_as_dictionary.append(dictionary_rb)
    return jsonify(results_as_dictionary)



# LOGOUT ROUTE



# These are the routes for the manager side.
@app.get("/manager/reimbursements")
def view_all_reimbursement_requests():
    all_reimbursements = manager_service.service_view_all_reimbursement_requests()
    rb_as_dictionaries = []
    for all_rb in all_reimbursements:
        dictionary_reimbursements = all_rb.reimbursement_dictionary()
        rb_as_dictionaries.append(dictionary_reimbursements)
    return jsonify(rb_as_dictionaries)


app.run()