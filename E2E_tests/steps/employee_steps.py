import time
from behave import Given, When, Then


# LOGGING IN
@Given(u'the employee is on the login page')
def get_login_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/index.html")


@When(u'the employee inputs 7 into the employee id input box')
def get_emp_username_input_box(context):
    context.employee_page.select_input_id_box().send_keys("7")


@When(u'the employee inputs whatever into the password input box')
def get_emp_password_input_box(context):
    context.employee_page.select_input_password_box().send_keys("whatever")


@When(u'the employee clicks the login button')
def select_login_button(context):
    context.employee_page.click_login_button().click()


@Then(u'the employee is redirected to the Employee Home page')
def get_employee_home_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Employee Home"





# SUBMITTING A NEW REIMBURSEMENT REQUEST
@Given(u'the employee is on the employee home page')
def get_employee_home_page(context):
    context.driver.get("file:///C:/Users/kckar/Desktop/Revature/project1_reimbursements/front-end/employee-home.html")


@When(u'the employee clicks the request reimbursement tab')
def select_request_reimbursement_tab(context):
    context.employee_page.click_request_reimbursement_tab().click()


@When(u'the employee inputs office supplies in the request purpose input')
def fill_request_purpose(context):
    context.employee_page.select_request_purpose_input().send_keys("office supplies")


@When(u'the employee inputs 46.89 in the amount input')
def fill_amount(context):
    context.employee_page.select_amount_input().send_keys("46.89")


@When(u'the employee clicks the submit reimbursement button')
def select_submit_reimbursement_button(context):
    context.employee_page.click_submit_reimbursement_button().click()


@Then(u'a new reimbursement request has been submitted and the employee is on the Employee Home page')
def request_submitted(context):
    title = context.driver.title
    assert title == "Employee Home"




# VIEWING EMPLOYEE'S REIMBURSEMENT REQUESTS
# @Given(u'the employee is on the employee home page')

@When(u'the employee clicks the view reimbursements tab')
def select_view_reimbursements_tab(context):
    context.employee_page.click_view_reimbursement_tab().click()


@Then(u'the reimbursements are shown and the employee is on the Employee Home page')
def reimbursements_are_shown(context):
    title = context.driver.title
    assert title == "Employee Home"




# LOGGING OUT
# @Given(u'the employee is on the employee home page')

@When(u'the employee clicks on the logout button')
def select_logout_button(context):
    context.employee_page.click_logout_button().click()


@Then(u'the employee will be redirected to the index Home page')
def employee_is_logged_out(context):
    assert context.driver.title == "Home"
